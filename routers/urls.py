from controllers.pages_controller import PagesController, CssController
from routers.router import Router

router = Router()
router.get('/', PagesController, 'home')
router.get('/css', CssController, 'css')
router.get('/add', PagesController, 'add')
router.post('/', PagesController, 'home')
router.get('/stats', PagesController, 'stats')
