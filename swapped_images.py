import os
import shutil

# Folder containing your images (adjust if needed)
folder = "assets/images"

# Supported image types
extensions = (".jpg", ".jpeg", ".png", ".webp")

for filename in os.listdir(folder):
    if "_optimized_" in filename:
        original_name = filename.replace("_optimized_", "")
        original_path = os.path.join(folder, original_name)
        optimized_path = os.path.join(folder, filename)
        large_path = os.path.join(folder, original_name.replace(".", "-LARGE."))

        # Only proceed if original exists
        if os.path.exists(original_path):
            print(f"Renaming {original_name} → {original_name.replace('.', '-LARGE.')}")
            shutil.move(original_path, large_path)

        # Rename optimized → original
        print(f"Replacing {original_name} with optimized version")
        shutil.move(optimized_path, original_path)

print("✅ All optimized images swapped successfully!")
