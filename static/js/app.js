document.addEventListener('DOMContentLoaded',()=>{
  document.body.addEventListener('click',e=>{
    const b=e.target.closest('.edit-btn');
    if(!b) return;
    const ds=b.dataset;
    document.getElementById('editTitle').value=ds.title;
    document.getElementById('editDescription').value=ds.desc;
    document.getElementById('editDone').checked = ds.done==="1";
    document.getElementById('editForm').action=`/edit/${ds.id}`;
    document.getElementById('editModal').style.display='flex';
  });
  document.getElementById('editCancel').onclick=()=>{
    document.getElementById('editModal').style.display='none';
  };
});
