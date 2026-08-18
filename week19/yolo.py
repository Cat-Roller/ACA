# from roboflow import Roboflow
# rf = Roboflow(api_key="4yGfOAtr5AflNwW8BB6T")
# project = rf.workspace("roboflow-universe-projects").project("license-plate-recognition-rxg4e")
# version = project.version(13)
# dataset = version.download("yolo26")

# rf = Roboflow(api_key="4yGfOAtr5AflNwW8BB6T")
# project = rf.workspace("prathama").project("chess-41fqv")
# version = project.version(1)
# dataset = version.download("yolo26")

from ultralytics import YOLO

model = YOLO('yolo26n.pt')

result = model.train(
    data = 'Chess.v1\data.yaml',
    #if you have cpu good enough increase the number of epochs to 30
    epochs = 5,
    imgsz = 640,
    batch = 8
)

print(result)
                