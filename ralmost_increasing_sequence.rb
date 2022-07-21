def solution(sequence)
  return true if sequence.length < 3

  return apply_check(sequence, false)
end

def apply_check(asequence, removed)
  puts(asequence)
  puts(removed)
  for i in 0..(asequence.length-2)
    puts(asequence[i])
    if (asequence[i] >= asequence[i + 1]) && !removed
      puts('inside recursion')
      sublist = asequence
      sublist.delete_at(i)
      puts('sublist', sublist)
      apply_check(sublist, true)
    elsif (asequence[i] >= asequence[i + 1]) && removed
      puts('Inside output')
      return false
    end
  end

  return true
end

puts('Calling method')
output = solution([1,3,2,1])

puts('Output: ', output)