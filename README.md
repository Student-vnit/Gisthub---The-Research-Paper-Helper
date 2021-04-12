[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper">
    <img src="src/logo.jpeg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Gisthub---The-Research-Paper-Helper</h3>

  <p align="center">
    why read when you can listen
    <br />
    <a href="https://sites.google.com/students.vnit.ac.in/gisthub/home"><strong>Explore the website »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper/issues">Report Bug</a>
    ·
    <a href="https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
    <li><a href="#what-we-learned">What We Learned</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

GistHub is a tool, our team has made for the betterment and ease of the tedious process of consuming research papers on the go.

It has two main functionalities :

- Research paper to audiobook conversion.
- Summarization of the research paper into a single paragraph.

### Built With

- [Heroku](https://dashboard.heroku.com)
- [FastAPI](https://fastapi.tiangolo.com)
- [ngrok](https://ngrok.com)
- [Google Colab](https://colab.research.google.com)
- [React](https://reactjs.org)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Install heroku-cli for your operating system.

### Installation

1. Clone the repo:
   ```sh
   git clone https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper.git
   ```
2. Initialize heroku repo:
   ```sh
   heroku create
   ```
3. Already existing app's remote can be added as remote using:
   ```sh
   heroku git:remote -a your_remote
   ```
4. Add support for apt-based dependencies during both compile and runtime.
   ```sh
   heroku buildpacks:add --index 1 heroku-community/apt
   ```
   <!-- USAGE EXAMPLES -->

## Usage

- Open the colab notebook [SUMMARIZER.ipynb](https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper/SUMMARIZER.ipynb) in Google Colab and start the ngrok server. Note the ngrok _url_ and replace app.py/initsummary/colab_url with url.
- Deploy to heroku:

  ```sh
  git push heroku master
  ```

- Change directory to ./softlab4, change remote url to your heroku url.

- Start the server:
  ```
  npm install
  ```
  ```
  npm run
  ```

Access server at [localhost:3000](localhost:3000) and now you can upload and get audio, summary and text.

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Abhishek Kumar Yadav - [github/abhk943](https://github.com/abhk943) - abhk943@gmail.com

Vanshika Jain - [github/Vanshika-30](https://github.com/Vanshika-30) - jvanshika30@gmail.com

Hardik Bhatia - [github/hardik2000](https://github.com/hardik2000) - hardikbhatia2000@gmail.com

Suyash Khade - [github/Suyash1700](https://github.com/Suyash1700) - suyukhade@gmail.com

Warun Panpaliya - [github/warun1801](https://github.com/warun1801) - warun1801@gmail.com

Shraddha Bhagwat - [github/shraddhab29](https://github.com/shraddhab29) - shraddhabhagawat2001@gmail.com

Abhishek Jaiswal - [github/abhishekjaiswal55236](https://github.com/abhishekjaiswal55236) - abhishekjaiswal55236@gmail.com

Samruddhi - [github@samruddhipande111](https://github.com/shraddhab29) - samruddhipande111@gmail.com

<br /><br />

Project Link: [https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper](https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper)

Website Link: [https://sites.google.com/students.vnit.ac.in/gisthub/home](https://sites.google.com/students.vnit.ac.in/gisthub/home)

<!-- WHAT WE LEARNED -->

## What We Learned

- Deploying app on **_Heroku_**, with custom apt packages and pip packages.
- Deploying machine learning based web-api usi **_Flask-ngrok_** and **_Google Colab_**.
- Building web-app with **_React-js_** and communicating with web requests.
- Creating **_FastAPI_** server to upload, process and serve basic files such as text, pdf and audio.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/Student-vnit/Gisthub---The-Research-Paper-Helper.svg?style=for-the-badge
[contributors-url]: https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Student-vnit/Gisthub---The-Research-Paper-Helper.svg?style=for-the-badge
[forks-url]: https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper/network/members
[stars-shield]: https://img.shields.io/github/stars/Student-vnit/Gisthub---The-Research-Paper-Helper.svg?style=for-the-badge
[stars-url]: https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper/stargazers
[issues-shield]: https://img.shields.io/github/issues/Student-vnit/Gisthub---The-Research-Paper-Helper.svg?style=for-the-badge
[issues-url]: https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper/issues
[license-shield]: https://img.shields.io/github/license/Student-vnit/Gisthub---The-Research-Paper-Helper.svg?style=for-the-badge
[license-url]: https://github.com/Student-vnit/Gisthub---The-Research-Paper-Helper/blob/master/LICENSE.txt
