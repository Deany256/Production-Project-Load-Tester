from locust import HttpUser, task, between
import random

# Asynchronous version


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)  # Wait time between tasks

    # List of login credentials
    login_credentials = [
        {"username": "user1", "password": "1234"},
        {"username": "new_user", "password": "password123"},
        # Add more credentials as needed
    ]

    @task(5)
    def view_product_list(self):
        self.client.get("/products")

    @task
    def view_product_details(self):
        product_id = random.randint(1, 100)  # Assuming product IDs range from 1 to 100
        self.client.get(f"/products/{product_id}")

    @task
    def add_product(self):
        payload = {"name": "New Product", "quantity": 10, "price": "10.99"}
        self.client.post("/add_product", data=payload)

    @task
    def delete_product(self):
        product_id = random.randint(1, 100)  # Assuming product IDs range from 1 to 100
        self.client.post(f"/products/{product_id}/delete")

    @task
    def edit_product(self):
        product_id = random.randint(1, 100)  # Assuming product IDs range from 1 to 100
        payload = {"name": "Edited Product", "quantity": 20, "price": "19.99"}
        self.client.post(f"/products/{product_id}/edit", data=payload)

    @task
    def signup(self):
        payload = {"username": "new_user", "password": "password123"}
        self.client.post("/signup", data=payload)

    @task
    def login(self):
        credentials = random.choice(self.login_credentials)
        payload = {
            "username": credentials["username"],
            "password": credentials["password"],
        }
        self.client.post("/login", data=payload)

    @task
    def logout(self):
        self.client.get("/logout")

    @task
    def access_protected_route(self):
        self.client.get("/protected")
