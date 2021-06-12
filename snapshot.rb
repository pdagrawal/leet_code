class Snapshot
  def initialize(array)
    @array = array.dup
  end

  def restore
    @array.dup
  end
end

array = [1, 2]
snap = Snapshot.new(array)
array[0] = 3
array = snap.restore()
puts array.join() #It should log "1,2"
array.push(4)
array = snap.restore()
puts array.join() #It should log "1,2"
