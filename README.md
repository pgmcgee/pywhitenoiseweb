# pywhitenoiseweb

Inspired by https://github.com/Relkci/ps-whitenoiseweb

The program runs a loop to open a popular link in Firefox about once a minute (random), occasionally taking a long break. It is bundled into a single statically linked binary that can be deployed to other hosts. This is useful to generate organic-ish looking traffic in a lab environment.

## How to Use

1. Install pipenv
2. Run `make install`
3. If you want to deploy, create a deploy.sh file (and make it executable)
3. Run `make` to build and deploy (if deploy.sh exists)
