<div id="top"></div>

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
<div align="center">
  <a href="https://github.com/isbd/Youtube_Tracker">
    <!--<img src="images/logo.png" alt="Logo" width="80" height="80">-->
  </a>

<h3 align="center">Youtube_Tracker</h3>

  <p align="center">
    An automated data collection tool for youtube
    <br />
    <!--
    <a href="https://github.com/isbd/Youtube_Tracker"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/isbd/Youtube_Tracker">View Demo</a>
    ·
    <a href="https://github.com/isbd/Youtube_Tracker/issues">Report Bug</a>
    ·
    <a href="https://github.com/isbd/Youtube_Tracker/issues">Request Feature</a>-->
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!--<li><a href="#acknowledgments">Acknowledgments</a></li>-->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Youtube bot for collecting data on channels and videos for analysis
<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)-->



<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python3](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Create a google project with a generated Youtube Data API v3 Token, Install python3 and pip install requirements.

### Prerequisites

* python
  ```sh
  WIP
  ```
* Google project with generated Youtube Data API v3 Token

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/isbd/Youtube_Tracker.git
   ```
2. Install google_api_python_client
   ```sh
   pip install google-api-python-client
   ```
3. Enter your API in `config.ini`
   ```ini
   [youtube]
   api_token='example_token'
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

WIP

<!--_For more examples, please refer to the [Documentation](https://example.com)_-->

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [X] API Connection
    - [X] Config File
- [X] Collect Specified Channel Data
- [ ] Collect Specified Video Data
    - [ ] Pull Transcripts
    - [ ] Transcript Analysis
      - [ ] Confidence Percentage

See the [open issues](https://github.com/isbd/Youtube_Tracker/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Currently not accepting contributions
<!--
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request-->

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ian Buchanan-Dempsey - [@BuchananDempsey](https://twitter.com/BuchananDempsey)

Project Link: [https://github.com/isbd/Youtube_Tracker](https://github.com/isbd/Youtube_Tracker)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!--
## Acknowledgments
* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>-->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/isbd/Youtube_Tracker.svg?style=for-the-badge
[contributors-url]: https://github.com/isbd/Youtube_Tracker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/isbd/Youtube_Tracker.svg?style=for-the-badge
[forks-url]: https://github.com/isbd/Youtube_Tracker/network/members
[stars-shield]: https://img.shields.io/github/stars/isbd/Youtube_Tracker.svg?style=for-the-badge
[stars-url]: https://github.com/isbd/Youtube_Tracker/stargazers
[issues-shield]: https://img.shields.io/github/issues/isbd/Youtube_Tracker.svg?style=for-the-badge
[issues-url]: https://github.com/isbd/Youtube_Tracker/issues
[license-shield]: https://img.shields.io/github/license/isbd/Youtube_Tracker.svg?style=for-the-badge
[license-url]: https://github.com/isbd/Youtube_Tracker/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
