---
layout:     post
title:      "Python Crash Course Part II: Proj 1 - Doge Invasion"
subtitle:   " \"from Alien invasion\""
date:       2019-03-23 10:00:00
author:     "Mugen"
header-img: "img/post-bg-os-metro.jpg"
tags:
    - Python Application
    - Book Notes
---

> A basic python game using Pygame library


# 12. A Ship that Fires Bullets

> In this chapter, you’ll set up Pygame and then create a ship that moves right and left, and fires bullets in response to player input.

### Creating a Pygame Window and Responding to User Input

The `screen object` is called a surface. A `surface` in Pygame is a part of the screen where you display a game element. Each element in the game, like the aliens or the ship, is a surface.

The game is controlled by a `while loop` that contains an event loop and code that manages screen updates.

To make our program respond to events, we’ll write an `event loop` to listen for an event and perform an appropriate task depending on the kind of event that occurred.

### Setting the Background Color

### Creating a Settings Class

### Adding the Ship Image

In Pygame, the origin (0, 0) is at the top-left corner of the screen.

### Refactoring

In larger projects, you’ll often `refactor` code you’ve written before adding more code. `Refactoring` simplifies the structure of the code you’ve already written, making it easier to build on.

### Responding to a Keypress

Each keypress is registered as a `KEYDOWN` event.

### Allowing Continuous Movement

We’ll know when the right arrow key is released by having our game detect a `pygame.KEYUP` event.

Then use the `KEYDOWN` and `KEYUP` events together with a flag called `moving_right` to implement continuous motion.

### Adjusting the Ship’s Speed

However, rect attributes such as `centerx` store only integer values.

Only the integer portion of `self.center` will be stored in `self.rect.centerx`.

(So, I don't know the reason we tried so much, but still ccan only keep the interger part.)

### Creating the Bullet Class

The bullet is not based on an image so we have to build a rect from scratch using the `pygame.Rect()` class. This class requires the x- and y-coordinates of the top-left corner of the `rect`, and the width and height of the `rect`.

### Storing Bullets in a Group

Now that we have a `Bullet` class and the necessary settings defined, we can write code to fire a bullet each time the player presses the spacebar. First, we’ll create a group in `alien_invasion.py` to store all the live bullets so we can manage the bullets that have already been fired. This group will be an instance of the class `pygame.sprite.Group`, which behaves like a list with some extra functionality that’s helpful when building games. We’ll use this group to draw bullets to the screen on each pass through the main loop and to update each bullet’s position.

### Firing Bullets

In `game_functions.py`, we need to modify `check_keydown_events()` to fire a bullet when the spacebar is pressed. We also need to modify `update_screen()` to make sure each bullet is redrawn to the screen before we call `flip()`.


# 13. Aliens!

The first row is offset to the left, which is actually good for gameplay because we want the fleet to move right until it hits the edge of the screen, then drop down a bit, then move left, and so forth. Like the classic game *Space Invaders*, this movement is more interesting than having the fleet drop straight down.

### Making the Fleet Move

To move the aliens, we’ll use an `update()` method in `alien.py`, which we’ll call for each alien in the group of aliens.

### Creating Settings for Fleet Direction & Checking to See Whether an Alien Has Hit the Edge

Now we’ll create the settings that will make the fleet move down the screen and to the left when it hits the right edge of the screen.

### Shooting Aliens

#### detecting bullet collisions

In game programming, `collisions` happen when game elements overlap. To make the bullets shoot down aliens, we’ll use the method `sprite.groupcollide()` to look for collisions between members of two groups.

The `sprite.groupcollide()` method compares each bullet’s `rect` with each alien’s `rect` and returns a dictionary containing the bullets and aliens that have collided. Each key in the dictionary is a bullet, and the corresponding value is the alien that was hit.

#### repopulating the fleet

To make a new fleet of aliens appear after a fleet has been destroyed, first check to see whether the group `aliens` is empty. If it is, we call `create_fleet()`. We’ll perform this check in `update_bullets()` because that’s where individual aliens are destroyed.

### Ending the Game

We’ll limit the number of ships a player can use and we’ll destroy the ship when an alien reaches the bottom of the screen. We’ll end the game when the player has used up all their ships.

#### Detecting Alien-Ship Collisions

Check for alien-ship collisions immediately after updating the position of each alien.

### Identifying When Parts of the Game Should Run


# 14. Scoring

> We’ll add a Play button to start a game on demand or to restart a game once it ends. We’ll also change the game so it speeds up when the player moves up a level, and we’ll implement a scoring system.

### Adding the Play Button

#### Creating a Button Class

Because Pygame doesn’t have a built-in method for making buttons, we’ll write a `Button` class to create a filled rectangle with a label.

#### Drawing the Button to the Screen

Create the button directly in `alien_invasion.py` if the game is inactive.

#### Starting the Game

To start a new game when the player clicks Play.

#### Resetting the Game

To reset the game each time the player clicks Play, we need to reset the game statistics, clear out the old aliens and bullets, build a new fleet, and center the ship.

#### Deactivating the Play Button

One issue with our Play button is that the button region on the screen will continue to respond to clicks even when the Play button isn’t visible. Click the Play button area by accident once a game has begun and the game will restart!

To fix this, set the game to start only when `game_active` is False.

### Leveling Up

### Scoring

> In this chapter you learned to build a Play button to start a new game and how to detect mouse events and hide the cursor in active games. You can use what you’ve learned to create other buttons in your games, like a Help button to display instructions on how to play. You also learned how to modify the speed of a game as it progresses, how to implement a progressive scoring system, and how to display information in textual and nontextual ways.
