package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	fmt.Println("Welcome to the GoPassword Generator!")

	// Get user input
	var lettersCount, symbolsCount, numbersCount int
	fmt.Print("How many letters would you like in your password? ")
	fmt.Scan(&lettersCount)
	fmt.Print("How many symbols would you like in your password? ")
	fmt.Scan(&symbolsCount)
	fmt.Print("How many numbers would you like in your password? ")
	fmt.Scan(&numbersCount)

	letters := "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	symbols := "!@#$%^&*()-_+=[]{}|;:,.<>?/"
	numbers := "0123456789"

	var password []string
	for i := 0; i < lettersCount; i++ {
		randomLetter := string(letters[rand.Intn(len(letters))])
		password = append(password, randomLetter)
	}

	for i := 0; i < symbolsCount; i++ {
		randomSymbol := string(symbols[rand.Intn(len(symbols))])
		password = append(password, randomSymbol)
	}

	for i := 0; i < numbersCount; i++ {
		randomNumber := string(numbers[rand.Intn(len(numbers))])
		password = append(password, randomNumber)
	}

	rand.Shuffle(len(password), func(i, j int) {
		password[i], password[j] = password[j], password[i]
	})
	finalPassword := strings.Join(password, "")
	fmt.Printf("Your password is: %s\n", finalPassword)
}
