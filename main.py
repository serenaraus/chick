import torch

def main():
    # Creating two tensors (like vectors of data)
    x = torch.tensor([1.0, 2.0, 3.0])
    y = torch.tensor([4.0, 5.0, 6.0])

    # Adding them together
    z = x + y
    print("Result:", z)

if __name__ == "__main__":
    main()
    