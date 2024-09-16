# simpleLMS
Simple least mean squares(LMS) and filtered least mean squares(FxLMS) algorithm.

# Useage
### LMS
```python
import simpleLMS
Pz = simpleLMS.LMS(data,record_data,0.02,filterSize)
Pz,test_error = simpleLMS.LMS(data,record_data,0.02,filterSize,True)
```
### FxLMS
```python
import simpleLMS
Wh = simpleLMS.FxLMS(data,record_data,SzW,0.002,filterSize)
Wh,test_error = simpleLMS.FxLMS(data,record_data,SzW,0.002,filterSize,True)
```
# Result
## LMS
### Error history
![image](https://github.com/user-attachments/assets/c3a45b98-7a1f-46fd-b142-5f39ee9adf35)
### Estimated filter Bode plot
![image](https://github.com/user-attachments/assets/7e8885e7-6b22-43ea-bfec-6f1fb369c0df)


### FxLMS
### Error history
![image](https://github.com/user-attachments/assets/1865d56e-1014-40f4-a00d-ec5ae892e68e)
### Estimated filter Bode plot
![image](https://github.com/user-attachments/assets/60150074-d388-4da8-8d7a-6b28e65d09b4)






