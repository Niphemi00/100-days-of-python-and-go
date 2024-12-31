package main

import (
	"fmt"
	"math/rand"
	"time"
	"strings"
)


func main() {
	// Seed the random generator
	rand.Seed(time.Now().UnixNano())
	options := []string{"rock", "paper", "scissors"}

	// Get computer's choice
	computerChoice := strings.ToLower(options[rand.Intn(len(options))])

	// Get human's choice
	var humanChoice string
	fmt.Println("Enter your choice (rock, paper, scissors):")
	fmt.Scanln(&humanChoice)
	humanChoice = strings.ToLower(humanChoice)

	// Determine the result
	if computerChoice == humanChoice {
		fmt.Printf("You picked %s, the computer picked %s...It's a draw!!!\n", humanChoice, computerChoice)
	} else if computerChoice == "rock" && humanChoice == "paper" {
		fmt.Printf("You picked %s, the computer picked %s...Hurray You won!!\n", humanChoice, computerChoice)
	} else if computerChoice == "paper" && humanChoice == "scissors" {
		fmt.Printf("You picked %s, the computer picked %s...Hurray You won!!\n", humanChoice, computerChoice)
	} else if computerChoice == "scissors" && humanChoice == "rock" {
		fmt.Printf("You picked %s, the computer picked %s...Hurray You won :)!!\n", humanChoice, computerChoice)
	} else {
		fmt.Printf("You picked %s, the computer picked %s...Sorry...You Lose ( ...\n", humanChoice, computerChoice)
	}
}