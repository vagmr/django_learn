const fs = require('fs')
const path = require('path')

distDir = path.join(__dirname, 'dist')
rootDir = path.join(__dirname, '../')

templatesDir = path.join(rootDir, 'templates')
staticDir = path.join(rootDir, 'static')
srcStaticDir = path.join(distDir, 'static/')

function moveFiles(srcDir, destDir) {
    // Create the destination directory if it doesn't exist
    fs.mkdirSync(destDir, { recursive: true });

    // Get all files and directories within the source directory
    const entries = fs.readdirSync(srcDir, { withFileTypes: true });

    // Move each entry to the destination directory
    entries.forEach(entry => {
        const srcPath = path.join(srcDir, entry.name);
        const destPath = path.join(destDir, entry.name);

        if (entry.isDirectory()) {
            // Recursively move files from subdirectories
            moveFiles(srcPath, destPath);
            // Remove the subdirectory after its contents have been moved
            fs.rmdirSync(srcPath);
        } else {
            // Move the file
            fs.renameSync(srcPath, destPath);
        }
    });
}
moveFiles(srcStaticDir, staticDir);
// Move all files from distDir to templatesDir
moveFiles(distDir, templatesDir);

// Move all files from srcStaticDir to staticDir
