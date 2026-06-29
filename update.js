const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const photoMap = {
    "Nam Ma River Bridge (Houaphanh)": "assets/real_1.jpg",
    "Xiengkho Roads (Houaphanh)": "assets/real_2.png",
    "Na Khwai Village Road": "assets/real_3.png",
    "Hadxaifong Riverside Road": "assets/real_4.jpg",
    "Thong Haihin Airport Upgrade": "assets/real_7.png",
    "450-Year Road Connector": "assets/real_6.jpg",
    "Pakngum District Roads": "assets/real_5.png"
};

html = html.replace(/<article class="project-entry">[\s\S]*?<h5 class="project-entry-name" data-en="([^"]+)"([^>]*)>([^<]+)<\/h5>/g, (match, enTitle, restAttrs, innerHTML) => {
    
    // Look up exactly in the map, otherwise keep what it had or fallback
    let imgSrc = photoMap[enTitle];
    
    if (!imgSrc) {
        // If not explicitly mapped, try to extract existing src to not overwrite
        let imgMatch = match.match(/<img src="([^"]+)"/);
        if (imgMatch) {
            imgSrc = imgMatch[1];
        } else {
            imgSrc = 'assets/building_construction.png';
        }
    }
    
    return `<article class="project-entry">
                    <div class="project-img-wrap">
                        <img src="${imgSrc}" alt="${enTitle}" class="project-card-img">
                    </div>
                    <h5 class="project-entry-name" data-en="${enTitle}"${restAttrs}>${innerHTML}</h5>`;
});

fs.writeFileSync('index.html', html);
console.log('Update complete with real photos.');
