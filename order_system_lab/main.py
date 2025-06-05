from order_system.facade import OrderProcessor

if __name__ == "__main__":
    order_type = input("Enter order type (physical/digital): ").strip()
    order_id = input("Enter order ID: ").strip()

    processor = OrderProcessor(order_type)
    result = processor.process_order(order_id)
    print(result)