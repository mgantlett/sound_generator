# sound_generator# White Noise Generator

## Overview
The White Noise Generator is a web application designed to create different types of noise, including white, pink, and brown noise. It uses the Web Audio API and is compatible with 7.1 surround sound systems. The application features adjustable frequency bands and automated fade-in and fade-out effects for a smooth audio experience.

## Features
- Generate white, pink, and brown noise.
- Support for 7.1 surround sound systems.
- Customizable frequency bands.
- Fade-in and fade-out audio effects.
- Presets for various use cases like speech masking, traffic noise reduction, workplace concentration, and relaxation.
- Save and load custom settings.

## How to Use
1. Open the application in a compatible web browser.
2. Select the desired noise type using the radio buttons.
3. Adjust the frequency bands using the sliders.
4. Click "Initialize Audio" to start the noise generation.
5. Use the preset buttons for specific scenarios or create your own settings.
6. Click "Stop Audio" to smoothly fade out and stop the noise generation.

## Technical Details
The application uses the Web Audio API, featuring a script processor node for noise generation and gain nodes for frequency band control. It supports 7.1 surround sound output. The user interface is built with HTML, CSS, and JavaScript, leveraging noUiSlider for interactive sliders.

### Key Functions
- `playNoise`: Initializes and starts the noise generation.
- `setupGainNodes`: Configures the gain nodes for frequency control.
- `generateWhiteNoise`, `generatePinkNoise`, `generateBrownNoise`: Functions for generating different types of noise.
- `stopNoise`: Gradually fades out and stops the noise.
- `toggleAudio`: Toggles audio playback on and off.
- `saveSettings`, `loadSettings`: Functions to save and load custom slider settings.

## Browser Compatibility
The application is best experienced in modern web browsers like Chrome, Firefox, and Edge that support the Web Audio API.

## Contributing
Contributions to the White Noise Generator project are welcome. Follow standard procedures for contributing to open-source projects, including submitting pull requests for new features or bug fixes.

## License
[MIT License](LICENSE.md)

## Author
[Your Name or GitHub Username]

---

This README provides a basic overview of the project. You can expand it with more detailed instructions, screenshots, and any additional information relevant to users or contributors.
