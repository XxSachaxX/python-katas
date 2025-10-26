# Potter Kata - Book Store Discount Calculator

## Original Kata Description

Once upon a time there was a series of 5 books about a very English hero called Harry. (At least when this Kata was invented, there were only 5. Since then they have multiplied.) Children all over the world thought he was fantastic, and, of course, so did the publisher. So in a gesture of immense generosity to mankind (and to increase sales), they set up the following pricing model to take advantage of Harry's magical powers.

### Pricing Model

- **One copy** of any of the five books costs **8 EUR**
- **Two different books** from the series: **5% discount** on those two books
- **Three different books**: **10% discount**
- **Four different books**: **20% discount**
- **Five different books**: **25% discount**

### Important Note

If you buy, say, four books, of which 3 are different titles, you get a 10% discount on the 3 that form part of a set, but the fourth book still costs 8 EUR.

### The Challenge

Potter mania is sweeping the country and parents of teenagers everywhere are queueing up with shopping baskets overflowing with Potter books. Your mission is to write a piece of code to calculate the price of any conceivable shopping basket.

---

## Custom Enhancements

I extended the original kata with additional requirements for fun:

### 1. Configurable Book Series

The solution supports any book series, not just Harry Potter. Book series are defined as configuration objects.

**Examples:**
- `books_series_configurations/harry_potter.py` - Original Harry Potter series
- `books_series_configurations/realm_of_the_elderlings.py` - Alternative fantasy series

Each series configuration defines the list of available books in the series.

### 2. Customizable Discount Structures

Discount rules are completely configurable through biller configurations, allowing for:
- Different discount percentages
- Varying base prices per book
- Alternative pricing strategies (e.g., Black Friday sales)

**Examples:**
- `biller_configurations/default.py` - Original kata pricing (5%, 10%, 20%, 25%)
- `biller_configurations/black_friday.py` - Custom promotional pricing

Each biller configuration defines:
- `base_amount_per_book()`: The price of a single book
- `discounts()`: Dictionary of discount rules with required book counts and multipliers

---

## License

Educational kata project - Feel free to use and modify.
