# LiDM-Based Baseline Generator

This folder is for notes and lightweight helper code for the LiDM-based generator work in the Sim2Real LiDAR challenge.
The main generator implementation will come from the official LiDM / LiDAR-Diffusion codebase. We are keeping that repo separate from this project repo.

LiDM repo: https://github.com/hancyran/LiDAR-Diffusion

## Goal

Train/adapt LiDM on allowed V2X-Real LiDAR frames so it can generate synthetic LiDAR point clouds. The generated point clouds can then be saved as `.bin` files and used as synthetic LiDAR data for the challenge pipeline.

### Extras
This folder also includes `demo_scene.json` and `utils.py`. These are not part of the core LiDM training pipeline right now but could come in use in the future during further implementation 
