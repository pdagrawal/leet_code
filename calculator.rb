# calculator.sum(23).subtract(3).multiply(2).result() should output 40
# calculator.sum(10, 30).subtract(15).multiply(6).result() should output 150
# calculator.sum(10, 10, 3, 5).multiply(2).subtract(5).result() should output 51
# calculator.sum(10, 10, 3, 5).result() should output 28


class Calculator
  def initialize
    @result = 0
  end

  def sum(*numbers)
    numbers.each do |num|
      @result += num
    end
    self
  end
end

calculator = Calculator.new
puts calculator.sum(23,1,2)

