package main

import (
	"net/http"
)

func main() {
	h := http.FileServer(http.Dir("C:\\"))
	http.ListenAndServe(":8080", h)
}
