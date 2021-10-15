<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<!--<div align="center">
  <a href="https://github.com/TheRealDarkCoder/ZoomBot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>-->

<h3 align="center">Zoom Bot</h3>

  <p align="center">
    This is my attempt of a keyboard macro based automated Zoom Meeting Joiner. This can just join a meeting at any specified scheduled time.
    <br />
    <a href="https://github.com/TheRealDarkCoder/ZoomBot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/TheRealDarkCoder/ZoomBot">View Demo</a>
    ·
    <a href="https://github.com/TheRealDarkCoder/ZoomBot/issues">Report Bug</a>
    ·
    <a href="https://github.com/TheRealDarkCoder/ZoomBot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Feel free to expand on it.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* Python 3

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You need python3 installed and some sort of Window manager/GUI Functionality, as well as Zoom Installed. Your input fields have to be focussable using tab on keyboard.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/TheRealDarkCoder/ZoomBot.git
   ```
2. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Enter your configuration in `timing.txt`
   ```text
   HH:MM,<MEETING ID>,<PASSWORD>,USERNAME
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Once you have the setup, run the python script `python3 main.py` or double click the `autostart.bat` (Windows only)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TheRealDarkCoder/ZoomBot.svg?style=for-the-badge
[contributors-url]: https://github.com/TheRealDarkCoder/ZoomBot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TheRealDarkCoder/ZoomBot.svg?style=for-the-badge
[forks-url]: https://github.com/TheRealDarkCoder/ZoomBot/network/members
[stars-shield]: https://img.shields.io/github/stars/TheRealDarkCoder/ZoomBot.svg?style=for-the-badge
[stars-url]: https://github.com/TheRealDarkCoder/ZoomBot/stargazers
[issues-shield]: https://img.shields.io/github/issues/TheRealDarkCoder/ZoomBot.svg?style=for-the-badge
[issues-url]: https://github.com/TheRealDarkCoder/ZoomBot/issues
[license-shield]: https://img.shields.io/github/license/TheRealDarkCoder/ZoomBot.svg?style=for-the-badge
[license-url]: https://github.com/TheRealDarkCoder/ZoomBot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png