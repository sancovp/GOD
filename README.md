# GOD

## REIFIED AGENTS
I am calling this type of agent "reified":

#### Background
LLMs consistently tend to fail with handling exact transformations from disparate information across longer contexts. Instead of trying to fix that, we can use a **Tree of Prompts** to construct **reified agents**. 

#### Usefulness
In agentic systems, context management should be a scale invariant pattern. The way to achieve this is with range, meaninig very constricted contexts with just enough complexity and no concepts outside of its completable loops and their reinforcement apparati, which is up to the prompt engineer. If the contexts are constricted to an exact transformation step that has a polymorphic input (for example, instead of writing every prompt for every animal with its specific sound, using a sound function that takes any animal string and outputs a generation of the sound, so the prompt that handles this transformation step function call in the tree of prompts is called "animal_sound"), then you can easily build an ontology, and you can process your input -> self API -> language models -> self API -> output loop as cognition directly, as reasoning.

#### Process
To **construct a reified agent**:
1) Diagram the exact context as concisely as possible (using a programming language shorthand dialect if context is long).
2) Then, give it a way to write shorthand that is understandable, meaning a way to talk about the domain that is specific enough to start to prime itself.
3) Ask new instances what it means. If it is wrong, tell it it's wrong and have it construct the proper representation.
4) Update the reification (ie 'how to generate an animal_sound'). Repeat until the semantics are so clear that it is a tautology that self-processes into an emergent you can steer.

(Note: there are a lot of tasks that models can already do immediately without being reified first, but that is not helpful for large assemblies and for that it is more helpful to reify even the small capacities of the models at hand.)
