# AutoFarmOS

## Installing Nanpy
First, you'll need to install setuptools for python, using the command

    python -m pip install --upgrade pip setuptools wheel

Additionally, you'll need to install the PySerial library with the command

    pip install pyserial

Finally, install the nanpy library on the Raspberry Pi,

    pip install nanpy

After completing the installation, following the instructions on the [Nanpy Repository](https://github.com/nanpy/nanpy) to build the firmware and upload it on the Arduino.

## Testing

Run the **blinky** test using the command

    python2 blinky.py

See a basic prototype reading of the liquid level sensor data with the command

    python2 liquid_level.py