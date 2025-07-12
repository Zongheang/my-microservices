package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello from Go Messenger Service")
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":3002", nil)
}
