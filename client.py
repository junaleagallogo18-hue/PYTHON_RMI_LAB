import Pyro5.api


def main():
    print("Client is starting...")

    try:
        # Find the remote laptop object.
        laptop = Pyro5.api.Proxy("PYRONAME:laptop")

        # Call the remote object's methods.
        name = laptop.getName()
        description = laptop.getDescription()
        price = laptop.getPrice()

        # Display the information received from the server.
        print("\n--- PRODUCT DETAILS ---")
        print("Name:", name)
        print("Description:", description)
        print("Price:", price)

    except Exception as error:
        print("Error connecting to server:", error)


if __name__ == "__main__":
    main()
