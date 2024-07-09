package main

import "fmt"

// Variables globales
var complejo complex64 = 4.7+6.2i
var arreglo = []int{10, 20, 30}
var flotante float64 = 8.15
var entero int = 11

func main() {
    if entero > 10 || flotante == 1.23 {
        var cadena string = "Hola Soledad"
        for i := 0; i < 2; i++ {
            entero += i * int(flotante) / 2
        }

        if flotante <= 5 {
            fmt.Println(cadena)
        } else {
            fmt.Println(entero, complejo)
        }
    }
}