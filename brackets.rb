class Brackets
  def self.paired?(brackets)
    pairs = { '{' => '}', '[' => ']', '(' => ')' }
    brackets = brackets.chars
    length = brackets.length
    return false unless length % 2 == 0

    (0...length/2).each do |index|
      return false unless pairs[brackets[index]] == brackets[length - index - 1]
    end
    true
  end
end

Brackets.paired?('{({][]})}[()]{}')
Brackets.paired?('{[([{{{()}}}])]}')
