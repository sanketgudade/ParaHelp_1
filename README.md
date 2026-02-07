# ParaHelp  
An IoT-Based Assistive Communication System

---

## Introduction

ParaHelp is an IoT-based assistive communication system designed for people who are paralyzed or have severe mobility limitations. Individuals who cannot move from their place often face serious challenges in communicating their basic needs, emergency requirements, or requests for assistance.

ParaHelp enables such individuals to communicate effectively using minimal physical input methods such as touch-based interaction and eye blink detection. The system converts these inputs into real-time notifications that are sent directly to the caretaker’s mobile device, ensuring timely assistance.

---

## Problem Statement

People with paralysis or restricted mobility often struggle to communicate their needs due to limited motor control. Conventional communication methods are not always accessible, leading to delayed responses and increased dependency on caregivers.

There is a need for a simple, reliable, and low-effort communication system that allows such individuals to express their needs without requiring physical movement or speech.

---

## Proposed Solution

ParaHelp provides a dual-input IoT-based solution using:
• A capacitive touch-based IoT mouse  
• Sensor-based eye blink detection glasses  

The system captures user input, processes it through computer software and a web application, and sends real-time notifications to caretakers through mobile alerts.

---

## System Architecture

The ParaHelp system follows a dual-input IoT-based architecture to support users with varying levels of mobility.

### 1. IoT-Based Touch Input Device
A small IoT-based mouse is designed using a capacitive touch sensor. This device allows users to provide input through minimal touch or pressure. The sensor detects the touch and sends the input signal to a connected computer or mobile device.

Once the input is received, the software processes the request and identifies the specific requirement. A real-time notification corresponding to the selected requirement is then sent to the caretaker’s registered mobile number.

### 2. Sensor-Based Eye Blink Input System
The second input mechanism consists of sensor-enabled smart glasses. These glasses detect eye blinks using integrated sensors. Based on predefined blink patterns, the system captures user intent and transfers the input to the computer software developed by our team.

The software interprets the blink input and triggers the appropriate alert. The corresponding notification is immediately sent to the caretaker’s mobile device via the communication backend.

### Communication Flow
• User provides input using touch device or eye blink sensor  
• Input is captured by the hardware sensors  
• Data is transmitted to the computer or mobile device  
• Software processes and maps the input to a requirement  
• Notification is sent to the caretaker’s mobile number  

This architecture ensures reliable, low-effort communication for users with severe physical limitations.

---

## Hardware Components

• Arduino Micro Pro  
• Capacitive Touch Sensor  
• IR / Eye Blink Sensor  
• Sensor-enabled Smart Glasses  
• Power supply and connecting wires  

---

## Software Components

• Arduino IDE  
• Python  
• Flask  
• PHP  
• HTML  
• CSS  
• JavaScript  

---

## Tech Stack

### Frontend
• HTML  
• CSS  
• JavaScript  
• Chart.js for data visualization  
• Image and Audio-based interface for message interaction  

### Backend
• PHP for backend logic and data storage  
• Flask for Message passing  

---

## How the System Works

• User interacts using minimal touch or eye blink  
• Sensors detect and capture the input  
• Input is transferred to the computer or mobile device  
• Backend processes the request  
• Relevant alert is generated  
• Notification is sent to the caretaker’s mobile number  

---

## Applications

• Hospitals and healthcare centers  
• Home care for paralyzed individuals  
• Rehabilitation centers  
• Elderly care facilities  

---

## Advantages

• Minimal physical effort required  
• Real-time communication  
• Cost-effective and scalable  
• Easy to use  
• Improves response time and safety  

---

## Future Enhancements

• Mobile application integration    
• AI-based eye tracking  
• Cloud-based data storage  
• Wearable device optimization  

---

## Conclusion

ParaHelp provides a practical and efficient communication solution for people with paralysis or severe mobility limitations. By integrating IoT devices, sensor-based input, and real-time web communication, the system significantly improves independence, safety, and quality of care.

---

ParaHelp  
Enabling communication for people with limited mobility.
