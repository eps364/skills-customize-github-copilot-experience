
# 📘 Assignment: Games in Python – Hangman

## 🎯 Objetivo

Build a playable Hangman game to practice Python fundamentals: strings, loops, conditionals, random selection, and user input handling.

## 📝 Tarefas

### 🛠️ Core Hangman Engine

#### Description
Implement the main game loop for Hangman where a secret word is randomly chosen and the player guesses one letter at a time until they win or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined Python list (at least 8 words)
- Display current progress using underscores for unknown letters (e.g. `_ a _ _ m a n`)
- Accept single-letter guesses from the user (case-insensitive)
- Reveal all occurrences of correctly guessed letters
- Track remaining attempts (e.g. start with 6–8 wrong guesses allowed)
- End with a win message if the word is fully revealed
- End with a loss message showing the secret word if attempts reach zero

Example (sample run):

```
Secret word selected. Good luck!
Word: _ _ _ _ _ _
Attempts left: 6
Guess a letter: a
Good! a is in the word.
Word: _ a _ _ _ a
Attempts left: 6
Guess a letter: z
Sorry, z is not in the word.
Incorrect guesses: z
Attempts left: 5
...
You win! The word was hangman
```

**Skills practiced:** String manipulation, loops, conditionals, random selection

## ✅ Must Have's

Your game must:
- Randomly select words from a predefined list
- Accept letter guesses and show current progress (_ _ _ format)
- Track incorrect guesses remaining
- End when word is guessed or attempts exhausted
- Display win/lose messages
