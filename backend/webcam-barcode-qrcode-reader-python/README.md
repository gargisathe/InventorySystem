# Reading Barcode and QR Code Using Webcam, Python and OpenCV
The sample demonstrates how to create a simple Webcam Barcode and QR code reader in Python. OpenCV stitcher API is used to stitch multiple barcode and QR code results.

## License Activation
Get a desktop license key from [here](https://www.dynamsoft.com/customer/license/trialLicense?product=dbr) to activate [Dynamsoft Barcode Reader SDK](https://www.dynamsoft.com/barcode-reader/sdk-desktop-server/):

```python
BarcodeReader.init_license("DLS2eyJoYW5kc2hha2VDb2RlIjoiMjAwMDAxLTE2NDk4Mjk3OTI2MzUiLCJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInNlc3Npb25QYXNzd29yZCI6IndTcGR6Vm05WDJrcEQ5YUoifQ==")
```

## Installation

```
pip install opencv-python dbr
```


- [scanner.py]
    
    Use webcam to scan barcode and QR code in real-time.

    ![Python barcode and QR code reader]
- [stitcher.py]
    
    Get camera closer to scan more barcode and QR code precisely and then stitch them together as a panorama image.

    ![Python barcode and QR code reader with panorama stitching]
- [barcode_based_panorama.py]
    
    Concatenate images based on barcode and QR code detection results. No image processing algorithm used.
    
    ![concatenate barcode and QR code images]
    
- [barcode_reader.py]
    
    Used to read barcode and QR code from image files.
    



