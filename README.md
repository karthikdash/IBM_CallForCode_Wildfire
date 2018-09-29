In 2017 alone, California experienced 7,117 wildfires. That's over 505,000 acres burned. We do not have sufficient data to accurately measure or predict wildfires. Present models are highly inaccurate. We believe that by using localised sensor networks would significantly improve prediction models. Also, wildfire detection from these sensors can trigger an emergency broadcast to people in the vicinity and also provide safe, low temperature zone directions. A heat map can be a valuable resource for firefighters who can isolate and mitigate high temperature zones. Overall, the sensor mesh could have multi-layered benefits. Our main idea is to use inexpensive sensors which will measure temperature, humidity and detect flames. So, this can be deployed in high risk areas. The implementation would require an MCU (Micro Controller Unit) which interfaces with temperature, relative humidity sensors and flam detection sensors ( IR Spectrometer). The data is synchronised and transmitted through BLE (Bluetooth Low Energy) to a central server. This enables us to use coin cell powered sensors which could alternatively be powered by solar cells as well. The data from this mesh is funnelled into a Raspberry Pi which connects to the IBM Cloud using a Python Flask server. The cloud interlaces the temperature, humidity and flame data with the weather API. This provides a better prediction model overall. The temperature data can be used to notify residents in the vicinity either through a mobile app or emergency broadcast. Map directions are provided to the residents to reach a safe place for evacuation. We have stipulated that, a sensor module will cost less than $10 on scale.
