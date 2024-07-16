package com.example.listusb

import android.hardware.usb.UsbDevice
import android.hardware.usb.UsbManager
import android.os.Bundle
import android.util.Log
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.listusb.ui.theme.ListUsbTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            ListUsbTheme {
                var usbDevices by remember { mutableStateOf<List<UsbDevice>>(emptyList()) }

                Scaffold(
                    modifier = Modifier.fillMaxSize()
                ) { innerPadding ->
                    Column(
                        modifier = Modifier
                            .fillMaxSize()
                            .padding(innerPadding)
                            .padding(16.dp)
                    ) {
                        Button(onClick = {
                            usbDevices = listUsbDevices()
                        }) {
                            Text("List USB Devices")
                        }
                        Spacer(modifier = Modifier.height(16.dp))
                        UsbDeviceList(devices = usbDevices)
                    }
                }
            }
        }
    }

    private fun listUsbDevices(): List<UsbDevice> {
        val usbManager = getSystemService(USB_SERVICE) as UsbManager
        return usbManager.deviceList.values.toList()
    }
}

@Composable
fun UsbDeviceList(devices: List<UsbDevice>) {
    if (devices.isEmpty()) {
        Text("No USB devices connected")
    } else {
        LazyColumn {
            items(devices) { device ->
                Log.d("MainActivity", device.toString())
                Text(
//                    text = "Device Name: ${device.deviceName}\nVendor ID: ${device.vendorId}\nProduct ID: ${device.productId}\n",
                    text = device.toString(),
                    modifier = Modifier.padding(vertical = 8.dp)
                )
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    ListUsbTheme {
        var usbDevices by remember { mutableStateOf<List<UsbDevice>>(emptyList()) }

        Scaffold(
            modifier = Modifier.fillMaxSize()
        ) { innerPadding ->
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(innerPadding)
                    .padding(16.dp)
            ) {
                Button(onClick = {
                    // Simulate button click in preview
                    usbDevices = emptyList()
                }) {
                    Text("List USB Devices")
                }
                Spacer(modifier = Modifier.height(16.dp))
                UsbDeviceList(devices = usbDevices)
            }
        }
    }
}
