# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_beast', [dirname(__file__)])
        except ImportError:
            import _beast
            return _beast
        if fp is not None:
            try:
                _mod = imp.load_module('_beast', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _beast = swig_import_helper()
    del swig_import_helper
else:
    import _beast
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_beast.PI_swigconstant(_beast)
PI = _beast.PI

_beast.TWOPI_swigconstant(_beast)
TWOPI = _beast.TWOPI

def load_config(filename):
    return _beast.load_config(filename)
load_config = _beast.load_config

def xyz_hash(x, y, z):
    return _beast.xyz_hash(x, y, z)
xyz_hash = _beast.xyz_hash

def xyz_hash_mask(radians):
    return _beast.xyz_hash_mask(radians)
xyz_hash_mask = _beast.xyz_hash_mask
class star(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, star, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, star, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _beast.star_x_set
    __swig_getmethods__["x"] = _beast.star_x_get
    if _newclass:
        x = _swig_property(_beast.star_x_get, _beast.star_x_set)
    __swig_setmethods__["y"] = _beast.star_y_set
    __swig_getmethods__["y"] = _beast.star_y_get
    if _newclass:
        y = _swig_property(_beast.star_y_get, _beast.star_y_set)
    __swig_setmethods__["z"] = _beast.star_z_set
    __swig_getmethods__["z"] = _beast.star_z_get
    if _newclass:
        z = _swig_property(_beast.star_z_get, _beast.star_z_set)
    __swig_setmethods__["flux"] = _beast.star_flux_set
    __swig_getmethods__["flux"] = _beast.star_flux_get
    if _newclass:
        flux = _swig_property(_beast.star_flux_get, _beast.star_flux_set)
    __swig_setmethods__["id"] = _beast.star_id_set
    __swig_getmethods__["id"] = _beast.star_id_get
    if _newclass:
        id = _swig_property(_beast.star_id_get, _beast.star_id_set)
    __swig_setmethods__["px"] = _beast.star_px_set
    __swig_getmethods__["px"] = _beast.star_px_get
    if _newclass:
        px = _swig_property(_beast.star_px_get, _beast.star_px_set)
    __swig_setmethods__["py"] = _beast.star_py_set
    __swig_getmethods__["py"] = _beast.star_py_get
    if _newclass:
        py = _swig_property(_beast.star_py_get, _beast.star_py_set)
    __swig_setmethods__["unreliable"] = _beast.star_unreliable_set
    __swig_getmethods__["unreliable"] = _beast.star_unreliable_get
    if _newclass:
        unreliable = _swig_property(_beast.star_unreliable_get, _beast.star_unreliable_set)
    __swig_setmethods__["star_idx"] = _beast.star_star_idx_set
    __swig_getmethods__["star_idx"] = _beast.star_star_idx_get
    if _newclass:
        star_idx = _swig_property(_beast.star_star_idx_get, _beast.star_star_idx_set)
    __swig_setmethods__["sigma_sq"] = _beast.star_sigma_sq_set
    __swig_getmethods__["sigma_sq"] = _beast.star_sigma_sq_get
    if _newclass:
        sigma_sq = _swig_property(_beast.star_sigma_sq_get, _beast.star_sigma_sq_set)
    __swig_setmethods__["hash_val"] = _beast.star_hash_val_set
    __swig_getmethods__["hash_val"] = _beast.star_hash_val_get
    if _newclass:
        hash_val = _swig_property(_beast.star_hash_val_get, _beast.star_hash_val_set)

    def __init__(self, *args):
        this = _beast.new_star(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __eq__(self, s):
        return _beast.star___eq__(self, s)

    def __mul__(self, s):
        return _beast.star___mul__(self, s)

    def DBG_(self, s):
        return _beast.star_DBG_(self, s)
    __swig_destroy__ = _beast.delete_star
    __del__ = lambda self: None
star_swigregister = _beast.star_swigregister
star_swigregister(star)
cvar = _beast.cvar


def star_gt_x(s1, s2):
    return _beast.star_gt_x(s1, s2)
star_gt_x = _beast.star_gt_x

def star_gt_y(s1, s2):
    return _beast.star_gt_y(s1, s2)
star_gt_y = _beast.star_gt_y

def star_gt_z(s1, s2):
    return _beast.star_gt_z(s1, s2)
star_gt_z = _beast.star_gt_z

def star_gt_flux(s1, s2):
    return _beast.star_gt_flux(s1, s2)
star_gt_flux = _beast.star_gt_flux

def star_lt_x(s1, s2):
    return _beast.star_lt_x(s1, s2)
star_lt_x = _beast.star_lt_x

def star_lt_y(s1, s2):
    return _beast.star_lt_y(s1, s2)
star_lt_y = _beast.star_lt_y

def star_lt_z(s1, s2):
    return _beast.star_lt_z(s1, s2)
star_lt_z = _beast.star_lt_z

def star_lt_flux(s1, s2):
    return _beast.star_lt_flux(s1, s2)
star_lt_flux = _beast.star_lt_flux
class star_db(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, star_db, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, star_db, name)
    __repr__ = _swig_repr
    __swig_setmethods__["max_variance"] = _beast.star_db_max_variance_set
    __swig_getmethods__["max_variance"] = _beast.star_db_max_variance_get
    if _newclass:
        max_variance = _swig_property(_beast.star_db_max_variance_get, _beast.star_db_max_variance_set)

    def __init__(self):
        this = _beast.new_star_db()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _beast.delete_star_db
    __del__ = lambda self: None

    def size(self):
        return _beast.star_db_size(self)

    def __iadd__(self, *args):
        return _beast.star_db___iadd__(self, *args)

    def __sub__(self, s):
        return _beast.star_db___sub__(self, s)

    def __and__(self, s):
        return _beast.star_db___and__(self, s)

    def get_star(self, idx):
        return _beast.star_db_get_star(self, idx)

    def copy(self):
        return _beast.star_db_copy(self)

    def copy_n_brightest(self, n):
        return _beast.star_db_copy_n_brightest(self, n)

    def load_catalog(self, catalog, year):
        return _beast.star_db_load_catalog(self, catalog, year)

    def count(self, *args):
        return _beast.star_db_count(self, *args)

    def DBG_(self, s):
        return _beast.star_db_DBG_(self, s)
star_db_swigregister = _beast.star_db_swigregister
star_db_swigregister(star_db)

class star_fov(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, star_fov, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, star_fov, name)
    __repr__ = _swig_repr

    def get_score(self, *args):
        return _beast.star_fov_get_score(self, *args)

    def get_id(self, px, py):
        return _beast.star_fov_get_id(self, px, py)

    def __init__(self, s, db_max_variance_):
        this = _beast.new_star_fov(s, db_max_variance_)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _beast.delete_star_fov
    __del__ = lambda self: None
star_fov_swigregister = _beast.star_fov_swigregister
star_fov_swigregister(star_fov)

class star_query(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, star_query, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, star_query, name)
    __repr__ = _swig_repr
    __swig_setmethods__["map"] = _beast.star_query_map_set
    __swig_getmethods__["map"] = _beast.star_query_map_get
    if _newclass:
        map = _swig_property(_beast.star_query_map_get, _beast.star_query_map_set)
    __swig_setmethods__["map_size"] = _beast.star_query_map_size_set
    __swig_getmethods__["map_size"] = _beast.star_query_map_size_get
    if _newclass:
        map_size = _swig_property(_beast.star_query_map_size_get, _beast.star_query_map_size_set)
    __swig_setmethods__["kdresults"] = _beast.star_query_kdresults_set
    __swig_getmethods__["kdresults"] = _beast.star_query_kdresults_get
    if _newclass:
        kdresults = _swig_property(_beast.star_query_kdresults_get, _beast.star_query_kdresults_set)

    def __init__(self, s):
        this = _beast.new_star_query(s)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _beast.delete_star_query
    __del__ = lambda self: None

    def is_kdsorted(self):
        return _beast.star_query_is_kdsorted(self)

    def kdsort(self):
        return _beast.star_query_kdsort(self)

    def sort(self):
        return _beast.star_query_sort(self)

    def r_size(self):
        return _beast.star_query_r_size(self)

    def get_kdmask(self, i):
        return _beast.star_query_get_kdmask(self, i)

    def reset_kdmask(self):
        return _beast.star_query_reset_kdmask(self)

    def clear_kdresults(self):
        return _beast.star_query_clear_kdresults(self)

    def kdcheck(self, idx, x, y, z, r, min_flux):
        return _beast.star_query_kdcheck(self, idx, x, y, z, r, min_flux)

    def kdsearch(self, *args):
        return _beast.star_query_kdsearch(self, *args)

    def kdsearch_x(self, x, y, z, r, min_flux, min, max):
        return _beast.star_query_kdsearch_x(self, x, y, z, r, min_flux, min, max)

    def kdsearch_y(self, x, y, z, r, min_flux, min, max):
        return _beast.star_query_kdsearch_y(self, x, y, z, r, min_flux, min, max)

    def kdsearch_z(self, x, y, z, r, min_flux, min, max):
        return _beast.star_query_kdsearch_z(self, x, y, z, r, min_flux, min, max)

    def kdmask_filter_catalog(self):
        return _beast.star_query_kdmask_filter_catalog(self)

    def kdmask_uniform_density(self, min_stars_per_fov):
        return _beast.star_query_kdmask_uniform_density(self, min_stars_per_fov)

    def from_kdmask(self):
        return _beast.star_query_from_kdmask(self)

    def from_kdresults(self):
        return _beast.star_query_from_kdresults(self)

    def DBG_(self, s):
        return _beast.star_query_DBG_(self, s)
star_query_swigregister = _beast.star_query_swigregister
star_query_swigregister(star_query)

class constellation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, constellation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, constellation, name)
    __repr__ = _swig_repr
    __swig_setmethods__["p"] = _beast.constellation_p_set
    __swig_getmethods__["p"] = _beast.constellation_p_get
    if _newclass:
        p = _swig_property(_beast.constellation_p_get, _beast.constellation_p_set)
    __swig_setmethods__["s1"] = _beast.constellation_s1_set
    __swig_getmethods__["s1"] = _beast.constellation_s1_get
    if _newclass:
        s1 = _swig_property(_beast.constellation_s1_get, _beast.constellation_s1_set)
    __swig_setmethods__["s2"] = _beast.constellation_s2_set
    __swig_getmethods__["s2"] = _beast.constellation_s2_get
    if _newclass:
        s2 = _swig_property(_beast.constellation_s2_get, _beast.constellation_s2_set)
    __swig_setmethods__["idx"] = _beast.constellation_idx_set
    __swig_getmethods__["idx"] = _beast.constellation_idx_get
    if _newclass:
        idx = _swig_property(_beast.constellation_idx_get, _beast.constellation_idx_set)

    def DBG_(self, s):
        return _beast.constellation_DBG_(self, s)

    def __init__(self):
        this = _beast.new_constellation()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _beast.delete_constellation
    __del__ = lambda self: None
constellation_swigregister = _beast.constellation_swigregister
constellation_swigregister(constellation)

class constellation_pair(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, constellation_pair, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, constellation_pair, name)
    __repr__ = _swig_repr
    __swig_setmethods__["totalscore"] = _beast.constellation_pair_totalscore_set
    __swig_getmethods__["totalscore"] = _beast.constellation_pair_totalscore_get
    if _newclass:
        totalscore = _swig_property(_beast.constellation_pair_totalscore_get, _beast.constellation_pair_totalscore_set)
    __swig_setmethods__["db_s1"] = _beast.constellation_pair_db_s1_set
    __swig_getmethods__["db_s1"] = _beast.constellation_pair_db_s1_get
    if _newclass:
        db_s1 = _swig_property(_beast.constellation_pair_db_s1_get, _beast.constellation_pair_db_s1_set)
    __swig_setmethods__["db_s2"] = _beast.constellation_pair_db_s2_set
    __swig_getmethods__["db_s2"] = _beast.constellation_pair_db_s2_get
    if _newclass:
        db_s2 = _swig_property(_beast.constellation_pair_db_s2_get, _beast.constellation_pair_db_s2_set)
    __swig_setmethods__["img_s1"] = _beast.constellation_pair_img_s1_set
    __swig_getmethods__["img_s1"] = _beast.constellation_pair_img_s1_get
    if _newclass:
        img_s1 = _swig_property(_beast.constellation_pair_img_s1_get, _beast.constellation_pair_img_s1_set)
    __swig_setmethods__["img_s2"] = _beast.constellation_pair_img_s2_set
    __swig_getmethods__["img_s2"] = _beast.constellation_pair_img_s2_get
    if _newclass:
        img_s2 = _swig_property(_beast.constellation_pair_img_s2_get, _beast.constellation_pair_img_s2_set)

    def flip(self):
        return _beast.constellation_pair_flip(self)

    def DBG_(self, s):
        return _beast.constellation_pair_DBG_(self, s)

    def __init__(self):
        this = _beast.new_constellation_pair()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _beast.delete_constellation_pair
    __del__ = lambda self: None
constellation_pair_swigregister = _beast.constellation_pair_swigregister
constellation_pair_swigregister(constellation_pair)

class constellation_lt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, constellation_lt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, constellation_lt, name)
    __repr__ = _swig_repr

    def __call__(self, c1, c2):
        return _beast.constellation_lt___call__(self, c1, c2)

    def __init__(self):
        this = _beast.new_constellation_lt()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _beast.delete_constellation_lt
    __del__ = lambda self: None
constellation_lt_swigregister = _beast.constellation_lt_swigregister
constellation_lt_swigregister(constellation_lt)


def constellation_lt_s1(c1, c2):
    return _beast.constellation_lt_s1(c1, c2)
constellation_lt_s1 = _beast.constellation_lt_s1

def constellation_lt_s2(c1, c2):
    return _beast.constellation_lt_s2(c1, c2)
constellation_lt_s2 = _beast.constellation_lt_s2

def constellation_lt_p(c1, c2):
    return _beast.constellation_lt_p(c1, c2)
constellation_lt_p = _beast.constellation_lt_p
class constellation_db(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, constellation_db, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, constellation_db, name)
    __repr__ = _swig_repr
    __swig_setmethods__["stars"] = _beast.constellation_db_stars_set
    __swig_getmethods__["stars"] = _beast.constellation_db_stars_get
    if _newclass:
        stars = _swig_property(_beast.constellation_db_stars_get, _beast.constellation_db_stars_set)
    __swig_setmethods__["results"] = _beast.constellation_db_results_set
    __swig_getmethods__["results"] = _beast.constellation_db_results_get
    if _newclass:
        results = _swig_property(_beast.constellation_db_results_get, _beast.constellation_db_results_set)
    __swig_setmethods__["map_size"] = _beast.constellation_db_map_size_set
    __swig_getmethods__["map_size"] = _beast.constellation_db_map_size_get
    if _newclass:
        map_size = _swig_property(_beast.constellation_db_map_size_get, _beast.constellation_db_map_size_set)
    __swig_setmethods__["map"] = _beast.constellation_db_map_set
    __swig_getmethods__["map"] = _beast.constellation_db_map_get
    if _newclass:
        map = _swig_property(_beast.constellation_db_map_get, _beast.constellation_db_map_set)

    def __init__(self, s, stars_per_fov, from_image):
        this = _beast.new_constellation_db(s, stars_per_fov, from_image)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _beast.delete_constellation_db
    __del__ = lambda self: None

    def DBG_(self, s):
        return _beast.constellation_db_DBG_(self, s)
constellation_db_swigregister = _beast.constellation_db_swigregister
constellation_db_swigregister(constellation_db)

class match_result(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, match_result, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, match_result, name)
    __repr__ = _swig_repr
    __swig_setmethods__["match"] = _beast.match_result_match_set
    __swig_getmethods__["match"] = _beast.match_result_match_get
    if _newclass:
        match = _swig_property(_beast.match_result_match_get, _beast.match_result_match_set)
    __swig_setmethods__["R11"] = _beast.match_result_R11_set
    __swig_getmethods__["R11"] = _beast.match_result_R11_get
    if _newclass:
        R11 = _swig_property(_beast.match_result_R11_get, _beast.match_result_R11_set)
    __swig_setmethods__["R12"] = _beast.match_result_R12_set
    __swig_getmethods__["R12"] = _beast.match_result_R12_get
    if _newclass:
        R12 = _swig_property(_beast.match_result_R12_get, _beast.match_result_R12_set)
    __swig_setmethods__["R13"] = _beast.match_result_R13_set
    __swig_getmethods__["R13"] = _beast.match_result_R13_get
    if _newclass:
        R13 = _swig_property(_beast.match_result_R13_get, _beast.match_result_R13_set)
    __swig_setmethods__["R21"] = _beast.match_result_R21_set
    __swig_getmethods__["R21"] = _beast.match_result_R21_get
    if _newclass:
        R21 = _swig_property(_beast.match_result_R21_get, _beast.match_result_R21_set)
    __swig_setmethods__["R22"] = _beast.match_result_R22_set
    __swig_getmethods__["R22"] = _beast.match_result_R22_get
    if _newclass:
        R22 = _swig_property(_beast.match_result_R22_get, _beast.match_result_R22_set)
    __swig_setmethods__["R23"] = _beast.match_result_R23_set
    __swig_getmethods__["R23"] = _beast.match_result_R23_get
    if _newclass:
        R23 = _swig_property(_beast.match_result_R23_get, _beast.match_result_R23_set)
    __swig_setmethods__["R31"] = _beast.match_result_R31_set
    __swig_getmethods__["R31"] = _beast.match_result_R31_get
    if _newclass:
        R31 = _swig_property(_beast.match_result_R31_get, _beast.match_result_R31_set)
    __swig_setmethods__["R32"] = _beast.match_result_R32_set
    __swig_getmethods__["R32"] = _beast.match_result_R32_get
    if _newclass:
        R32 = _swig_property(_beast.match_result_R32_get, _beast.match_result_R32_set)
    __swig_setmethods__["R33"] = _beast.match_result_R33_set
    __swig_getmethods__["R33"] = _beast.match_result_R33_get
    if _newclass:
        R33 = _swig_property(_beast.match_result_R33_get, _beast.match_result_R33_set)

    def __init__(self, db_, img_, img_mask_):
        this = _beast.new_match_result(db_, img_, img_mask_)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _beast.delete_match_result
    __del__ = lambda self: None

    def size(self):
        return _beast.match_result_size(self)

    def init(self, db_const_, img_const_):
        return _beast.match_result_init(self, db_const_, img_const_)

    def copy_over(self, c):
        return _beast.match_result_copy_over(self, c)

    def related(self, m):
        return _beast.match_result_related(self, m)

    def search(self):
        return _beast.match_result_search(self)

    def clear_search(self):
        return _beast.match_result_clear_search(self)

    def compute_score(self):
        return _beast.match_result_compute_score(self)

    def from_match(self):
        return _beast.match_result_from_match(self)

    def weighted_triad(self):
        return _beast.match_result_weighted_triad(self)

    def DBG_(self, s):
        return _beast.match_result_DBG_(self, s)

    def print_ori(self):
        return _beast.match_result_print_ori(self)
match_result_swigregister = _beast.match_result_swigregister
match_result_swigregister(match_result)

class db_match(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, db_match, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, db_match, name)
    __repr__ = _swig_repr
    __swig_setmethods__["p_match"] = _beast.db_match_p_match_set
    __swig_getmethods__["p_match"] = _beast.db_match_p_match_get
    if _newclass:
        p_match = _swig_property(_beast.db_match_p_match_get, _beast.db_match_p_match_set)
    __swig_setmethods__["winner"] = _beast.db_match_winner_set
    __swig_getmethods__["winner"] = _beast.db_match_winner_get
    if _newclass:
        winner = _swig_property(_beast.db_match_winner_get, _beast.db_match_winner_set)

    def __init__(self, db, img):
        this = _beast.new_db_match(db, img)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _beast.delete_db_match
    __del__ = lambda self: None
db_match_swigregister = _beast.db_match_swigregister
db_match_swigregister(db_match)

# This file is compatible with both classic and new-style classes.


