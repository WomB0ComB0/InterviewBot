from cohere.classify import Example
import cohere
co = cohere.Client('rQqHCRnyHOS8JLTNbvYPzdrSwqu6fb0qwxD4MXvu')

# 5. Why did you leave your previous job?
examples = [
    # bad
    Example("lorem", "Bad"),  # 1
    Example("lorem", "Bad"),  # 2
    Example("lorem", "Bad"),  # 3
    Example("lorem", "Bad"),  # 4
    Example("lorem", "Bad"),  # 5
    Example("lorem", "Bad"),  # 6
    Example("lorem", "Bad"),  # 7
    Example("lorem", "Bad"),  # 8
    Example("lorem", "Bad"),  # 9
    Example("lorem", "Bad"),  # 10
    Example("lorem", "Bad"),  # 11
    Example("lorem", "Bad"),  # 12
    Example("lorem", "Bad"),  # 13
    Example("lorem", "Bad"),  # 14
    Example("lorem", "Bad"),  # 15
    Example("lorem", "Bad"),  # 16
    Example("lorem", "Bad"),  # 17
    Example("lorem", "Bad"),  # 18
    Example("lorem", "Bad"),  # 19
    Example("lorem", "Bad"),  # 20

    # good
    Example("lorem", "Good"),  # 1
    Example("lorem", "Good"),  # 2
    Example("lorem", "Good"),  # 3
    Example("lorem", "Good"),  # 4
    Example("lorem", "Good"),  # 5
    Example("lorem", "Good"),  # 6
    Example("lorem", "Good"),  # 7
    Example("lorem", "Good"),  # 8
    Example("lorem", "Good"),  # 9
    Example("lorem", "Good"),  # 10
    Example("lorem", "Good"),  # 11
    Example("lorem", "Good"),  # 12
    Example("lorem", "Good"),  # 13
    Example("lorem", "Good"),  # 14
    Example("lorem", "Good"),  # 15
    Example("lorem", "Good"),  # 16
    Example("lorem", "Good"),  # 17
    Example("lorem", "Good"),  # 18
    Example("lorem", "Good"),  # 19
    Example("lorem", "Good"),  # 20

]

# manual entry for testing
inputs = [
    "lorem sucks",  # bad
    "lorem dumbass",  # bad
    "lorem love",  # good
    "lorem good"  # good
]

response = co.classify(
    model='medium',  # Consider changing to large?
    inputs=inputs,
    examples=examples)

print(response.classifications)
