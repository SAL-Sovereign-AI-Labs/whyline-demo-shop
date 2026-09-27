import csv


def export_orders(orders, path):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        for o in orders:
            w.writerow([o.total()])
