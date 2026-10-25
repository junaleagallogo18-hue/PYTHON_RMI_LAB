import Pyro5.api
from product import Product


def main():
    print("Server is booting....")

    # Create the product objects from the original Java program.
    p1 = Product("Laptop", "Lenovo laptop", 800000.0)
    p2 = Product("Mobile", "MI 9 mobile", 24000.0)
    p3 = Product("Bag", "Branded bag", 800.0)
    p4 = Product("Charger", "MI Charger", 230.0)

    # Start the Pyro5 server.
    daemon = Pyro5.api.Daemon()

    # Connect to the Pyro5 name server.
    ns = Pyro5.api.locate_ns()

    # Register each product as a remote object.
    daemon.register(p1, objectId="laptop")
    daemon.register(p2, objectId="mobile")
    daemon.register(p3, objectId="bag")
    daemon.register(p4, objectId="charger")

    ns.register("laptop", daemon.uriFor(p1))
    ns.register("ram", daemon.uriFor(p2))
    ns.register("bag", daemon.uriFor(p3))
    ns.register("charger", daemon.uriFor(p4))

    print("Products registered successfully!")
    print("Available products: laptop, ram, bag, charger")
    print("Server is ready for client requests.")

    # Keep the server running.
    daemon.requestLoop()


if __name__ == "__main__":
    main()
