from ultralytics import YOLO
import cv2

def main():
    model = YOLO('yolov8n.pt')
    
    print("Running detection on sample image...")
    results = model('https://ultralytics.com/images/bus.jpg')
    
    output_path = 'results.jpg'
    results[0].save(output_path)
    print(f"Detection completed. Results saved to {output_path}")
    
    img = cv2.imread(output_path)
    if img is not None:
        cv2.imshow('Detection Results', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Could not read the saved image at {output_path}")

if __name__ == "__main__":
    main()