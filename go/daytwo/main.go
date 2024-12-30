package main
import "fmt"

func main() {
	fmt.Println("Welcome to the tip calculator")
	var bill_amount float64
	var tip_amount float64	
	var payers_quantity int
	fmt.Print("What was the total bill? $")
	fmt.Scanln(&bill_amount)
	fmt.Print("How much tip (in percentage of bill) would you like to give 10, 12, or 15? ")
	fmt.Scanln(&tip_amount)
	tip_amount = (tip_amount / 100) * bill_amount
	bill_amount += tip_amount
	fmt.Print("How many people are to split the bill? ")
	fmt.Scanln(&payers_quantity)
	payers_share := bill_amount / float64(payers_quantity)
	fmt.Printf("Each person should pay: $%.2f\n", payers_share)
}