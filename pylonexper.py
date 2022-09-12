import pypylon.pylon as py

tlf = py.TlFactory.GetInstance()
cam = py.InstantCamera(tlf.CreateFirstDevice())

cam.Open()
print(cam.DeviceModelName.Value)

temp_sens = cam.DeviceTemperatureSelector.Symbolics

for sens in temp_sens:
    cam.DeviceTemperatureSelector = sens
    temp = cam.DeviceTemperature.Value 
    print(f"{sens} temp is {temp}°C")


# demonstrate some feature access
# new_width = cam.Width.GetValue() - cam.Width.GetInc()
# if new_width >= cam.Width.GetMin():
#     cam.Width.SetValue(new_width)

# numberOfImagesToGrab = 100
# cam.StartGrabbingMax(numberOfImagesToGrab)

# while cam.IsGrabbing():
#     grabResult = cam.RetrieveResult(5000, py.TimeoutHandling_ThrowException)

#     if grabResult.GrabSucceeded():
#         # Access the image data.
#         print("SizeX: ", grabResult.Width)
#         print("SizeY: ", grabResult.Height)
#         img = grabResult.Array
#         print("Gray value of first pixel: ", img[0, 0])

#     grabResult.Release()
# cam.Close()