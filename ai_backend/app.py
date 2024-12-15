from flask import Flask, request, jsonify
import os
from ultralytics import YOLO
from PIL import Image, ImageDraw

app = Flask(__name__)

# Load YOLO model directly
model = YOLO('yolov8n.pt')
model.conf = 0.25  # Confidence threshold
print(f"Model loaded: {model}")

@app.route('/detect', methods=['POST'])
def detect_objects():
    print("Received request to /detect endpoint")
    file = request.files['image']
    if not file:
        print("Error: No image uploaded")
        return jsonify({'error': 'No image uploaded'}), 400

    # Save image temporarily
    input_path = os.path.join('temp', file.filename)
    file.save(input_path)
    print(f"Image saved to: {input_path}")

    # Perform detection
    try:
        results = model(input_path)
    except Exception as e:
        print(f"Error during detection: {e}")
        return jsonify({'error': 'Object detection failed'}), 500

    # Process detections
    detections = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            detection = {
                'class': model.names[int(box.cls[0].item())],  # Class name
                'confidence': box.conf[0].item(),  # Confidence score
                'bbox': box.xyxy[0].tolist()  # Bounding box coordinates (x1, y1, x2, y2)
            }
            detections.append(detection)

    # Save results (draw bounding boxes on the image)
    output_path = os.path.join('output', file.filename)
    image = Image.open(input_path)
    draw = ImageDraw.Draw(image)
    for detection in detections:
        bbox = detection['bbox']
        draw.rectangle(bbox, outline="red", width=3)  # Draw bounding box
        draw.text((bbox[0], bbox[1]), f"{detection['class']} ({detection['confidence']:.2f})", fill="red")  # Add class and confidence
    image.save(output_path)
    print(f"Output image saved to: {output_path}")

    return jsonify({
        'detections': detections,
        'output_image': output_path
    })

if __name__ == '__main__':
    # Ensure temp and output directories exist
    os.makedirs('temp', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    app.run(host='0.0.0.0', port=5001)

