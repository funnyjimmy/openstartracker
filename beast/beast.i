%module beast
%{
#include "config.h"
#include "stars.h"
#include "constellations.h"
#include "beast.h"
%}
%include output.i
//newobject gives python control of these objects
%newobject star_db::copy;
%newobject star_db::copy_n_brightest;
%newobject star_query::from_kdmask;
%newobject star_query::from_kdresults;
%newobject match_result::from_match;
%include "config.h"
%include "stars.h"
%include "constellations.h"
%include "beast.h"
