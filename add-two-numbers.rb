require 'benchmark'

Benchmark.bm do |benchmark|
  benchmark.report("Logic") do
    def add_two_numbers(l1, l2)
      sum = 0
      l1.each_with_index do |num, index|
        sum += num * 10**index
      end
      l2.each_with_index do |num, index|
        sum += l2[index] * 10**index
      end
      sum.digits
    end

    add_two_numbers([2,4,3], [5,6,4])
    add_two_numbers([0], [0])
    add_two_numbers([9,9,9,9,9,9,9], [9,9,9,9])
    add_two_numbers([9,9,9,9,9,9,9], [9]*100000)
  end

  benchmark.report("Logic") do
    def add_two_numbers(l1, l2)
      sum = 0
      base = l1.length < l2.length ? l1 : l2
      base.each_with_index do |num, index|
        sum += num * 10**index
      end
      l1.each_with_index do |num, index|
        sum += num * 10**index
      end
      l2.each_with_index do |num, index|
        sum += l2[index] * 10**index
      end
      sum.digits
    end

    puts add_two_numbers([2,4,3], [5,6,4])
    puts add_two_numbers([0], [0])
    puts add_two_numbers([9,9,9,9,9,9,9], [9,9,9,9])
  end
end