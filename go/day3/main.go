package main
import "fmt"
import "strings"

func main() {
	fmt.Println("Welcome to Treasure Island! Your mission is to find the treasure!")

	fmt.Print("You are at a crossroad. Pick a path: left or right?\n")
	var crossRoad string
	fmt.Scanln(&crossRoad)
	strings.ToLower(crossRoad)

	if crossRoad == "left" {
		fmt.Print("You've come to a lake. There's an island in the middle of the lake.\nType 'swim' to swim across or 'wait' to wait for a boat: ")
		var moveToLake string 
		fmt.Scanln(&moveToLake)
		strings.ToLower(moveToLake)

		if moveToLake == "swim" {
			fmt.Println("You met an Electric eel, and it shocked you off the game....Game Over!!!")
		} else if moveToLake == "wait" {
			fmt.Print("Hurray!!! You made it across the lake.\nHere are three colors: pick any one to decide your fate (yellow, red, or blue): ")
			var colorChoice string
			fmt.Scanln(&colorChoice)
			strings.ToLower(colorChoice)
			if colorChoice == "red" {
				fmt.Println("You picked the fire pill...Sorry, You got burnt...Game Over!!!")
			} else if colorChoice == "yellow" {
				fmt.Println("You picked the treasure pill...Hurray, You found the treasure...Congrats!!!")
			} else if colorChoice == "blue" {
				fmt.Println("You picked the beast feast pill...Sorry, You got eaten by beasts...Game Over!!!")
			} else {
				fmt.Println("Invalid Input....Game ends!!!")
			}
		} else {
			fmt.Println("Invalid Input....Game ends!!!")
		}
	} else if crossRoad == "right" {
		fmt.Println("Sorry mate, You fell into a hole. Game Over!!!")
	} else {
		fmt.Println("Invalid Input....Game ends!!!")
	}
}
