class PeekingIterator implements Iterator<Integer> {
    private Iterator<Integer> ds;
    private Integer nextEl;
    private boolean nextAbsent;
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
        ds = iterator;
	    cacheNext();
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return nextEl;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
        Integer x = nextEl;
	    cacheNext();
        return x;
	}
	
	@Override
	public boolean hasNext() {
	    return !nextAbsent;
	}
    
    private void cacheNext(){
        if(ds.hasNext()){
            nextEl = ds.next();
        }
        else{
            nextAbsent = true;
        }
    }
}
