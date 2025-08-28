# RobotEvents Bot

## Overview
A Discord bot specifically made for the VEX Robotics Texas Region 4 community, intended to extend visibility and accessibility of tournament details to students and coaches alike.

## Developer Setup
In order to get started with this repository:

1. Create a new Discord bot ([tutorial here](https://discord.com/developers/docs/quick-start/getting-started))
2. Create a RobotEvents account and request API access
3. Inside the root directory, create an .env file and declare the following variables:
     - Your Discord bot token
     - Your RobotEvents API key
     - RobotEvents API endpoint
     - Working environment (For now, this can be set to anything other than 'prod'. This variable is used to deploy the bot on Google Cloud Run)

Please also install dependencies listed in requirements.txt.