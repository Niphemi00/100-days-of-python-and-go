package main
import "fmt"

func main() {
	// PROJECT ONE: BANDNAME GENERATOR
	fmt.Println("Welcome to the Band Name Generator.")
	var cityName string
	var petName string
	fmt.Println("What's the name of the city you grew up in? ")
	fmt.Scanln(&cityName)
	fmt.Println("What's your pet's name? ")
	fmt.Scanln(&petName)
	fmt.Printf("Your band name could be %s%s\n", cityName, petName)
}