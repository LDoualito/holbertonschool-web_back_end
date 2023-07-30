export default function cleanSet(set, startString) {
    if (typeof set !== 'object') return '';
    if (typeof startString !== 'string') return '';
    if (startString.length === 0) return '';
  
    const list = [];
    set.forEach((e) => {
      if (e && e.startsWith(startString)) list.push(e.replace(startString, ''));
      return e;
    });
    return list.join('-');
  }
