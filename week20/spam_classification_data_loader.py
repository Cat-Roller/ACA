import kagglehub

# Download latest version
smap_path = kagglehub.dataset_download("team-ai/spam-text-message-classification")

print("Path to dataset files:", smap_path)