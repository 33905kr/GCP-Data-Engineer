from google.cloud import bigquery


def query_public_dataset():
    client = bigquery.Client()

    query = """
    SELECT order_items.id, order_id, product_id, products.name
    FROM `bigquery-public-data.thelook_ecommerce.order_items` AS order_items
    JOIN `bigquery-public-data.thelook_ecommerce.products` AS products
    ON order_items.product_id = products.id
    """

    results = client.query(query).to_dataframe()[:5]

    
    print(results)


if __name__ == "__main__":
    query_public_dataset()