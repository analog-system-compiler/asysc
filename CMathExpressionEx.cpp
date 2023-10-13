/*******************************************************************************/
/*  Copyright (C) 2006 The SIMCAS project                                      */
/*                                                                             */
/*  This program is free software; you can redistribute it and/or modify       */
/*  it under the terms of the GNU General Public License as published by       */
/*  the Free Software Foundation; either version 2 of the License, or          */
/*  (at your option) any later version.                                        */
/*                                                                             */
/*  This program is distributed in the hope that it will be useful,            */
/*  but WITHOUT ANY WARRANTY; without even the implied warranty of             */
/*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              */
/*  GNU General Public License for more details.                               */
/*                                                                             */
/*  You should have received a copy of the GNU General Public License          */
/*  along with this program; if not, write to the Free Software                */
/*  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA. */
/*******************************************************************************/

#include "Element.h"
#include "CMathExpressionEx.h"
// #include "Derivative.h"
// #include "NonLinear.h"
// #include "NonLinDataBase.h"
// #include "DerivativeDataBase.h"

// void CMathExpressionEx::BinaryOperation(OP_CODE op, const CElement *e1)
// {
//   ASSERT(e1);
//   Zero();
//   Push(e1);
//   if (!RefToElement(op)->IsBinary())
//   {
//     Push(CElementDataBaseEx::OP_CONCAT);
//   }
//   Push(op);
//   OptimizeTree();
//   RemoveZero();
// }

// void CMathExpressionEx::RemoveBiasPoint()
// {
// #if 0
//   CEquation equ0( m_ElementDB );
//   CEquation equ1( m_ElementDB );

//   CElement* e = GetVariable( false );
//   if( e )
//   {
//     ToPolynom( e );
//     GetPower( equ0, 0 );
//     GetPower( equ1, 1 );
//     equ1.Mul( e );
//     equ0.RemoveBiasPoint();
//     equ0.Add( equ1 );
//     Copy( equ0 );
//   }
//   else
//   {
//     // end recursion with SRC()
//     ToPolynom( RefToElement( OP_SRC ) );
//     //replace SRC() by 1, equ0 set to 0
//     GetPower( equ1, 1 );
//     Copy( equ1 );
//   }
// #else
//   UnaryOperation(CElementDataBaseEx::OP_REMOVE_BIAS);
// #endif
// }

void CMathExpressionEx::ToPython(CParser& parser, CDisplay &ds)
{
  CElement *e;
  OP_CODE op_add=m_ElementDB->GetElement("ADD")->ToRef();
  OP_CODE op_sub=m_ElementDB->GetElement("SUB")->ToRef();
  Parse(parser);
  pos_t pos = m_StackSize;
  ds = "\t";
  while (pos != 0)
  {
    OP_CODE op = Pop(pos);
    if (op == op_add)
    {
      op = Pop(pos);
      e = m_ElementDB->RefToElement(op);
      ds += "\t";
      e->Display(ds);
      ds += "-(";
      DisplayBranch(ds, pos);
      ds += ");";
    }
    else if (op == op_sub)
    {
      op = Pop(pos);
      e = m_ElementDB->RefToElement(op);
      ds += "\t";
      e->Display(ds);
      ds += "";
      DisplayBranch(ds, pos);
      ds += ";";
    }
  }
}

// void CMathExpressionEx::DiffTransformation(const CMathExpressionEx &equ, const CTransform &transform, CDerivativeDataBase *db)
// {

//   CMathExpressionEx equ2(GetElementDB());
//   CMathExpressionEx equ3(GetElementDB());
//   CMathExpressionEx equ4(GetElementDB());

//   equ2.Copy(equ);
//   switch (transform.m_Transform)
//   {
//   case CTransform::TRANS:
//     equ2.UnaryOperation(CElementDataBaseEx::OP_TRANS);
//     break;
//   case CTransform::DC:
//     equ2.UnaryOperation(CElementDataBaseEx::OP_TRANS);
//     break;
//   case CTransform::AC:
//     equ2.UnaryOperation(CElementDataBaseEx::OP_AC);
//     break;
//   default:
//     ASSERT(false);
//   }

//   Clear();
//   pos_t pos = equ2.m_StackSize;
//   while (pos != 0)
//   {
//     OP_CODE op = equ2.Pop(pos);
//     equ4.Copy(*this);
//     if (op == CElementDataBaseEx::OP_TRANS1)
//     {
//       equ3.CopyBranch(equ2, pos);
//       CDerivative *deriv = db->GetDerivative(equ3);
//       if ((transform.m_Transform == CTransform::TRANS) && (deriv->m_Reference == transform.m_DerVariable))
//       {
//         Copy(deriv->m_ParamEquation);
//         Mul(deriv->m_Alpha);
//         Add(deriv->m_Beta);
//       }
//       else if ((transform.m_Transform == CTransform::DC) && (deriv->m_Reference == transform.m_DerVariable))
//       {
//         Clear();
//         Push(CElementDataBase::OP_ZERO);
//         // Push(deriv->m_Beta);
//       }
//       else
//       {
//         ASSERT(false);
//       }
//     }
//     else
//     {
//       Clear();
//       if ((transform.m_Transform == CTransform::DC) && (RefToElement(op) == transform.m_DerVariable))
//       {
//         op = CElementDataBase::OP_ZERO; // replace "t" by "0"
//       }
//       Push(op);
//     }

//     Append(equ4.m_StackArray, equ4.m_StackSize);
//   }

// #ifdef _DEBUG
//   CDisplay ds;
//   ds.Clear();
//   ds.Append("Transformation : ");
//   equ.Display(ds);
//   ds.Append("=0");
//   ds.Append(" -> ");
//   Display(ds);
//   ds.Append("=0");
//   TRACE(ds.GetBufferPtr());
// #endif
// }

// #if 0
// void CEquationEx::LogModule() // gives 10log(||)
// {
//   CEquation equR( m_ElementDB ), equI( m_ElementDB );

//   GetRealAndImag( equR, equI );
//   equR.BinaryOperation( OP_DB, equI );
//   Copy( equR );
// }

// void CEquationEx::Phase() // gives phase
// {
//   CEquation equR( m_ElementDB ), equI( m_ElementDB );

//   GetRealAndImag( equR, equI );
//   equR.BinaryOperation( OP_PHASE, equI );
//   Copy( equR );

// }
// #endif

// /* remplace les �l�ments par ceux correspondant dans le syst�me appelant */
// #if OPT33 == 1
// void CMathExpressionEx::Instanciate(const CMathExpression &equ1, const CElementArray &instance_list)
// {
//   unsigned pos, index;
//   OP_CODE op;
//   CElement *e1, *e2;
//   CMathExpression equ2(m_System);
//   CMathExpression equ3(m_System);

//   pos = equ1.m_StackSize;

//   if (pos)
//   {

//     op = equ1.PopOperator(pos);

//     if (IsElement(op))
//     {

//       e1 = (CElement *)equ1.PopElement(pos);

//       if (e1->IsConst() || e1->IsGlobal())
//       {
//         Init(e1);
//       }

//       else
//       {

//         index = e1->m_Index;
//         ASSERT(index < instance_list.GetSize());
//         e2 = instance_list.GetAt(index);

//         CMathExpression *equ5 = e2->GetEquation();

//         if (equ5)
//         {
//           Copy(*equ5);
//         }

//         else
//         {
//           Init(ElementToRef(e2));
//         }
//       }
//     }

//     else if (IsBinary(op))
//     {

//       equ2.CopyBranch(equ1, pos);
//       equ3.Instanciate(equ2, instance_list);
//       equ2.CopyBranch(equ1, pos);
//       Instanciate(equ2, instance_list);
//       BinaryOperation(op, equ3);
//     }

//     else if (IsUnary(op))
//     {

//       equ2.CopyBranch(equ1, pos);
//       Instanciate(equ2, instance_list);
//       UnaryOperation(op);
//     }

//     else
//     {
//       Init(op);
//     }
//   }

//   else
//   {
//     Clear();
//   }
// }
// #elif OPT33 == 2
// void CMathExpressionEx::Instanciate(const CMathExpression &equ1, const CElementArray &instance_list)
// {
//   unsigned pos;

//   Clear();

//   pos = equ1.m_StackSize;

//   if (pos)
//   {
//     Instanciate(equ1, instance_list, pos);
//   }

//   ASSERT(pos == 0);
// }

// void CMathExpressionEx::Instanciate(const CMathExpression &equ1, const CElementArray &instance_list, unsigned &pos)
// {
//   unsigned index;
//   OP_CODE op;
//   CElement *e1, *e2;

//   op = equ1.PopOperator(pos);

//   if (IsElement(op))
//   {

//     e1 = (CElement *)equ1.PopElement(pos);

//     if (e1->IsConst() || e1->IsGlobal())
//     {
//       PushElement(ElementToRef(e1));
//     }

//     else
//     {

//       index = e1->m_Index;
//       ASSERT(index < instance_list.GetSize());
//       e2 = instance_list.GetAt(index);

//       CMathExpression *equ5 = e2->GetEquation();

//       if (equ5)
//       {
//         PushEquation(*equ5);
//       }

//       else
//       {
//         PushElement(ElementToRef(e2));
//       }
//     }
//   }

//   else
//   {

//     if (IsBinary(op))
//     {

//       Instanciate(equ1, instance_list, pos);
//       Instanciate(equ1, instance_list, pos);
//     }

//     else if (IsUnary(op))
//     {
//       Instanciate(equ1, instance_list, pos);
//     }

//     PushOperator(op);
//   }
// }
// #elif OPT33 == 3
// void CMathExpressionEx::Instanciate(const CMathExpressionEx &equ1, const CElementArray &instance_list /*, const CEquationArray* equ_list*/)
// {
//   CElementDataBaseEx *db = equ1.GetElementDB();
//   CElement *e1, *e2;
//   ASSERT(instance_list.GetSize() == db->GetSize());
//   Copy(equ1);
//   for (unsigned i = 0; i < instance_list.GetSize(); i++)
//   {
//     e1 = db->GetAt(i);
//     e2 = instance_list.GetAt(i);
//     ASSERT(e2);
//     Replace(e1->ToRef(), e2->ToRef());
//   }
// #if _DEBUG
//   CDisplay ds;
//   ds.Append("Instanciate : ");
//   equ1.Display(ds);
//   ds.Append(" => ");
//   Display(ds);
//   TRACE(ds.GetBufferPtr());
// #endif
// #if 0
//   // TO DO : use Instanciate3 instead
//   unsigned  pos;
//   OP_CODE op;
//   CElement* e2;
//   CEquationEx equ4( m_ElementDB );

//   equ4.SetSize( equ1.GetSize() );
//   Clear();

//   pos = equ1.GetSize();

//   while( pos != 0 )
//   {

//     op = equ1.Pop( pos );
//     equ4.Copy( *this );
//     Clear();

//     e2 = instance_list.GetAt( RefToElement( op )-> );
//     /*if( equ_list && equ_list->GetAt( op ) )
//     {
//       Push( *equ_list->GetAt( op ) );
//     }
//     else*/
//     {
//       Push( ElementToRef( e2 ) );
//     }

//     Push( equ4 );
//   }
// #endif
// }
// #endif

// #if 1
// void CMathExpressionEx::Instanciate(const CMathExpressionEx &equ1, const CElement *e1, const CMathExpression *equ2)
// {
//   unsigned pos;
//   OP_CODE op;

//   ASSERT(equ2);
//   ASSERT(e1);
//   Clear();

//   for (pos = 0; pos != equ1.GetSize(); pos++) // see CMathExpression::Replace
//   {
//     op = equ1.Get(pos);
//     if (e1 == RefToElement(op))
//     {
//       Push(*equ2);
//     }
//     else
//     {
//       Push(op);
//     }
//   }
// }
// #else
// void CMathExpressionEx::Instanciate(const CMathExpressionEx &equ1, const CElement *e1, const CMathExpression *equ2)
// {
//   unsigned pos;
//   OP_CODE op;
//   CMathExpressionEx equ4(GetElementDB());

//   ASSERT(e1);
//   Clear();

//   pos = equ1.GetSize();

//   while (pos != 0)
//   {

//     op = equ1.Pop(pos);
//     equ4.Copy(*this);
//     Clear();

//     /*if( e1 == NULL )
//     {

//       CEquation* equ3 = e->GetEquation();

//       if( equ3 )
//       {
//         Push( *equ3 );
//       }

//       else
//       {
//         Push( op );
//       }

//     }

//     else */
//     if (e1 == RefToElement(op))
//     {

//       ASSERT(equ2);
//       Push(*equ2);
//     }

//     else
//     {
//       Push(op);
//     }

//     Push(equ4);
//   }
// }
// #endif

// void CMathExpressionEx::AllForcedExcept(CElementArrayEx &elem_array) const
// {
//   pos_t pos;
//   OP_CODE op;
//   CElement *e;

//   pos = GetSize();

//   while (pos != 0)
//   {

//     op = Pop(pos);
//     e = RefToElement(op);

//     if (elem_array.GetIndexOf(e) == elem_array.GetSize())
//     {
//       if (!e->IsConst())
//       {
//         e->SetFunct();
//       }
//     }

//     else
//     {
//       e->SetVar();
//     }
//   }
// }

// #if (OPT39 == 1)
// void CMathExpressionEx::GetNumAndDen(CMathExpression &equ_num, CMathExpression &equ_den) const
// {
//   unsigned pos;
//   OP_CODE op;

//   pos = m_StackSize;

//   if (pos)
//   {

//     op = PopOperator(pos);

//     if (op == OP_DIV)
//     {
//       equ_den.CopyBranch(*this, pos);
//       equ_num.CopyBranch(*this, pos);
//       ASSERT(pos == 0);
//     }

//     else
//     {
//       equ_num.Copy(*this);
//       equ_den.Init();
//     }
//   }

//   else
//   {
//     equ_num.Clear();
//     equ_den.Init();
//   }
// }
// #endif

// bool CMathExpressionEx::HasVariable(OP_CODE op1) const
// {
//   pos_t pos;
//   OP_CODE op2;

//   pos = GetSize();
//   while (pos != 0)
//   {

//     op2 = Pop(pos);

//     if (op2 == op1)
//     {
//       return true;
//     }
//   }

//   return false;
// }

// void CMathExpressionEx::Linearize(const CMathExpressionEx &equ1, CNonLinDataBase &ndb)
// {
//   CMathExpressionEx equ2(GetElementDB());
//   CMathExpressionEx equ3(GetElementDB());
//   CMathExpressionEx equ4(GetElementDB());

//   equ2.Copy(equ1);
//   equ2.UnaryOperation(CElementDataBaseEx::OP_LIN);

//   // equ4.SetSize( equ1.GetSize() );
//   Clear();
//   pos_t pos = equ2.m_StackSize;
//   while (pos != 0)
//   {
//     OP_CODE op = equ2.Pop(pos);
//     equ4.Copy(*this);
//     if (op == CElementDataBaseEx::OP_LIN1)
//     {
//       equ3.CopyBranch(equ2, pos);
//       CNonLinear *nonlin = ndb.GetNonLinear(equ3);
//       ApplyNonLinear(*nonlin);
//     }
//     else
//     {
//       Clear();
//       Push(op);
//     }

//     Append(equ4.m_StackArray, equ4.m_StackSize);
//   }

// #ifdef _DEBUG
//   CDisplay ds;
//   ds.Append("Linearize : ");
//   equ1.Display(ds);
//   ds.Append(" => ");
//   Display(ds);
//   TRACE(ds.GetBufferPtr());
// #endif
// }

// #if OPT42
// bool CMathExpressionEx::RemoveForcedBranches(CElementArray &elem_array, CEquationArrayEx &equ_array)
// {
//   // See IsForced()
//   CElement *e;
//   CMathExpressionEx equ1(GetElementDB());
//   CMathExpressionEx equ0(GetElementDB());

//   if (IsSimple()) // don't need to be replaced by aux variable
//   {
//     return false;
//   }

//   // Get Variables but not forced.
//   e = GetVariable(false);
//   if (e)
//   {
//     e->Lock();
//     ToPolynom(e);
//     equ0.GetPower(*this, 0);
//     equ1.GetPower(*this, 1);
//     equ0.RemoveForcedBranches(elem_array, equ_array);
//     equ1.RemoveForcedBranches(elem_array, equ_array);
//     equ1.Mul(e);
//     equ1.Add(equ0);
//     Copy(equ1);
//     e->Unlock();
//   }
//   else
//   {
//     e = m_ElementDB->GetElement();
//     e->SetFunct();
//     equ_array.Append(new CMathExpressionEx(*this));
//     elem_array.Append(e);
//     Init(e);
//   }

//   return true;
// }
// #endif

// void CMathExpressionEx::Normalize()
// {
//   CElement *e = RefToElement(CElementDataBaseEx::OP_LPL);
//   // BinaryOperation( CElementDataBaseEx::OP_POLY, e );
//   BinaryOperation(CElementDataBaseEx::OP_NORM, e);
// }

// CElement *CMathExpressionEx::GetElement() const
// {
//   CElement *e;
//   OP_CODE op;
//   pos_t pos = GetSize();

//   if (pos == 0)
//   {
//     op = CElementDataBaseEx::OP_ZERO;
//   }
//   else
//   {
//     op = Pop(pos);
//   }

//   if (pos == 0)
//   {
//     e = RefToElement(op);
//   }
//   else
//   {
//     e = NULL;
//   }

//   return e;
// }

// void CMathExpressionEx::ToPolynom(CElement *e)
// {
//   BinaryOperation(CElementDataBaseEx::OP_POLY, e);
// }

// void CMathExpressionEx::GetPower(const CMathExpressionEx &equ, unsigned power)
// {
//   Copy(equ);
//   CElement *e = GetElementDB()->RefToElement(power == 0 ? (OP_CODE)CElementDataBaseEx::OP_ZERO : (OP_CODE)CElementDataBaseEx::OP_ONE);
//   BinaryOperation(CElementDataBaseEx::OP_GET_POWER, e);
// }

// CElement *CMathExpressionEx::GetVariable(bool bForced) const
// {
// #if 1
//   pos_t pos = GetSize();
//   while (pos != 0)
//   {

//     OP_CODE op = Pop(pos);
//     CElement *e = RefToElement(op);

//     if (e && !e->IsLocked() && !e->IsConst() //|| AreConstAllowed() )  )
//         && (!e->IsFunct() || bForced))
//     {
//       return e;
//     }
//   }

//   return NULL;
// #else // doesn't detect forced var
//   CMathExpressionEx equ(*this);
//   equ.UnaryOperation(CElementDataBaseEx::OP_GET_VAR);
//   return equ.GetElement();
// #endif
// }

// bool CMathExpressionEx::IsSimple() const
// {
//   return GetUnknownNumber() < 2;
// }

// bool CMathExpressionEx::IsConst() const
// {
//   OP_CODE op = GetLastOperator();
//   CElement *e = RefToElement(op);
//   return e->IsConst();
// }

// unsigned CMathExpressionEx::GetUnknownNumber() const
// {
//   unsigned val = 0;

//   CElement *e = GetVariable();
//   if (e)
//   {
//     e->Lock();
//     val = GetUnknownNumber() + 1;
//     e->Unlock();
//   }

//   return val;
// }

// void CMathExpressionEx::ChangeToIf()
// {
//   pos_t pos = m_StackSize;
//   pos_t pos2 = pos;
//   CMathExpression equ(*this);

// #if _DEBUG
//   CDisplay ds;
//   Display(ds);
// #endif

//   pos2 = NextBranch(pos2);
//   m_StackSize = pos2;
//   Push(CElementDataBaseEx::OP_CONCAT);
//   Push(CElementDataBaseEx::OP_VECT);
//   PushBranch(equ, pos);
//   Push(CElementDataBaseEx::OP_AT);

// #if _DEBUG
//   ds.Clear();
//   Display(ds);
// #endif
// }
// /*
// void CMathExpressionEx::At( unsigned n )
// {
//   Push( CValue( n ) );
//   UnaryOperation( CElementDataBaseEx::OP_AT );
// }*/

// bool CMathExpressionEx::IsEqualTo(const CMathExpressionEx &equ) const
// {
//   return (m_StackSize == equ.GetSize()) && ((m_StackSize == 0) || !memcmp(m_StackArray, equ.m_StackArray, m_StackSize * sizeof(OP_CODE)));
// }

// bool CMathExpressionEx::GetNullEquation(CParser &IC)
// {
//   bool bOK;
//   // WARNING !! this function is not used by the system parser
//   // See CAnalysis::Evaluate
//   // GetLevel( IC, 0 ); //replaced by GetFromString

//   if (GetLastOperator() == CElementDataBaseEx::OP_EQV)
//   {
//     Pop(m_StackSize);
//     Push(CElementDataBaseEx::OP_SUB);
//     bOK = true;
//   }
//   else
//   {
//     bOK = false;
//   }

//   // Simplify(); // Allows functions to be replaced
//   return bOK;
// }

// void CMathExpressionEx::ExtractEquationList(CEquationArrayEx &list, OP_CODE separator) const
// {
//   CMathExpressionEx *equ;
//   pos_t pos = GetSize();
//   list.DeleteAll();

//   while (pos)
//   {
//     if (Pop(pos) != separator)
//     {
//       pos++;
//     }

//     equ = new CMathExpressionEx(GetElementDB());
//     equ->CopyBranch(*this, pos);
//     list.InsertAt(0, equ);
//   }
// }

// void CMathExpressionEx::ToEquation(const CEquationArrayEx &list, OP_CODE separator)
// {
//   Clear();

//   if (list.GetSize())
//   {
//     Push(*list[0]);
//     for (unsigned i = 1; i < list.GetSize(); i++)
//     {
//       Push(*list[i]);
//       Push(separator);
//     }
//   }
// }

// void CMathExpressionEx::ApplyNonLinear(CNonLinear &nonlin)
// {

// #if OPT27
//   // ASSERT( nonlin.m_Alpha );
//   if (nonlin.m_Alpha != NULL)
//   {
//     Clear();
//     Push(nonlin.m_ParamEquation); // x
//     Push(nonlin.m_Alpha);
//     Push(CElementDataBaseEx::OP_MUL);
//     ASSERT(nonlin.m_Beta);
//     Push(nonlin.m_Beta);
//     Push(CElementDataBaseEx::OP_ADD);
//   }
//   else
//   {
//     ASSERT(nonlin.m_Beta);
//     Clear();
//     Push(nonlin.m_Beta);
//   }
// #else
//   PushElement(ElementToRef(nonlin->m_Gamma));
//   PushOperator(OP_SUB);
//   PushElement(ElementToRef(nonlin->m_Alpha));
//   PushOperator(OP_MUL);
//   PushElement(ElementToRef(nonlin->m_Beta));
//   PushOperator(OP_ADD);
// #endif
// }

// void CMathExpressionEx::ApplyKirshoffLaws()
// {
// #ifdef _DEBUG
//   CDisplay ds;
//   Display(ds);
//   TRACE(ds.GetBufferPtr());
// #endif

//   // GetFromString("SYST( SYST( SYST( U-THROUGH(@1,@2) H-V-U ) P-U+V ) V-THROUGH(@1,@2))");
//   Simplify(); // Replace nodes
//   UnaryOperation(CElementDataBaseEx::OP_NODE_TRANS);
//   UnaryOperation(CElementDataBaseEx::OP_LOOP_TRANS);

// #ifdef _DEBUG
//   ds.Clear();
//   Display(ds);
//   TRACE(ds.GetBufferPtr());
// #endif
// }

// const CValue &CMathExpressionEx::EvaluateCplx() const
// {
//   CEvaluatorEx *eval = static_cast<CEvaluatorEx *>(m_ElementDB->GetEvaluator());
//   return eval->EvaluateCplx(m_StackSize, m_StackArray);
// }

// const CValue &CMathExpressionEx::Evaluate() const
// {
//   CMathExpression::Evaluate();
//   return m_ElementDB->GetEvaluator()->GetValue();
// }
