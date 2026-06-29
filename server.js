const express = require('express');
const multer = require('multer');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;
const DATA_FILE = path.join(__dirname, 'data.json');

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Static file serving for everything in current directory
app.use(express.static(__dirname));

// Multer Setup for Image Uploads
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        const uploadDir = path.join(__dirname, 'uploads');
        if (!fs.existsSync(uploadDir)) {
            fs.mkdirSync(uploadDir);
        }
        cb(null, uploadDir);
    },
    filename: (req, file, cb) => {
        const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
        const ext = path.extname(file.originalname);
        cb(null, 'activity-' + uniqueSuffix + ext);
    }
});
const upload = multer({ storage: storage });

// Helper to Read/Write Data
const readData = () => {
    if (!fs.existsSync(DATA_FILE)) {
        return [];
    }
    const raw = fs.readFileSync(DATA_FILE);
    try {
        return JSON.parse(raw);
    } catch (e) {
        return [];
    }
};

const writeData = (data) => {
    fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
};


// ----------------------------------------------------
// API ROUTES
// ----------------------------------------------------

// GET all activities
app.get('/api/activities', (req, res) => {
    const activities = readData();
    res.json(activities);
});

// POST a new activity (Title, Description, and Photo)
app.post('/api/activities', upload.single('photo'), (req, res) => {
    const { titleEn, titleLa, titleZh, descEn, descLa, descZh, date } = req.body;
    
    // Check for image
    let photoUrl = null;
    if (req.file) {
        photoUrl = '/uploads/' + req.file.filename;
    }

    const activities = readData();
    const newActivity = {
        id: Date.now().toString(),
        date: date || new Date().toISOString().split('T')[0],
        photoUrl: photoUrl,
        title: {
            en: titleEn || '',
            la: titleLa || '',
            zh: titleZh || ''
        },
        desc: {
            en: descEn || '',
            la: descLa || '',
            zh: descZh || ''
        },
        timestamp: Date.now()
    };
    
    // Add to top of list
    activities.unshift(newActivity);
    writeData(activities);

    res.json({ success: true, activity: newActivity });
});

// DELETE an activity by ID
app.delete('/api/activities/:id', (req, res) => {
    let activities = readData();
    const id = req.params.id;
    
    const activity = activities.find(a => a.id === id);
    if (activity && activity.photoUrl) {
        // Optionally delete the file
        const filePath = path.join(__dirname, activity.photoUrl);
        if (fs.existsSync(filePath)) {
            fs.unlinkSync(filePath);
        }
    }

    activities = activities.filter(a => a.id !== id);
    writeData(activities);
    res.json({ success: true });
});

// Start Server
app.listen(PORT, () => {
    console.log(`PSL Group Server running at http://localhost:${PORT}`);
});
